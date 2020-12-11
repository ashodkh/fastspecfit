#!/usr/bin/env python
"""Main module for nyxgalaxy.

ToDo:
* Generalize to work on coadded spectra.
* Fit to the photometry.
* Solve for vdisp, zcontinuum, and E(B-V).
* Add polynomial correction templates
* Capture ivar=0 problems.
* Correct for MW extinction.
* Fit Mg II.

ELG - 20200228 70005
BGS+MWS - 20200303 70500
BGS+MWS - 20200315 66003

new truth table for 70500 is here--
/global/cfs/cdirs/desi/sv/vi/TruthTables/Andes_reinspection/BGS

https://desi.lbl.gov/trac/wiki/SurveyValidation/TruthTables
https://desi.lbl.gov/DocDB/cgi-bin/private/RetrieveFile?docid=5720;filename=DESI_data_042820.pdf

time nyxgalaxy --tile 70500 --night 20200303 --nproc 32 --overwrite

time nyxgalaxy --tile 67230 --night 20200315 --nproc 32 --overwrite # ELG
time nyxgalaxy --tile 68001 --night 20200315 --nproc 32 --overwrite # QSO+LRG
time nyxgalaxy --tile 68002 --night 20200315 --nproc 32 --overwrite # QSO+LRG
time nyxgalaxy --tile 67142 --night 20200315 --nproc 32 --overwrite # ELG
time nyxgalaxy --tile 66003 --night 20200315 --nproc 32 --overwrite # BGS+MWS

time nyxgalaxy-qa --tile 67142 --night 20200315 --first 0 --last 10

"""
import pdb # for debugging

import os, sys, time
import numpy as np
import multiprocessing

from desiutil.log import get_logger
log = get_logger()

# ridiculousness!
import tempfile
os.environ['MPLCONFIGDIR'] = tempfile.mkdtemp()
import matplotlib
matplotlib.use('Agg')

def _nyxfit_one(args):
    """Multiprocessing wrapper."""
    return nyxfit_one(*args)

def nyxfit_one(indx, data, CFit, EMFit, out):
    """Fit one."""
    log.info('Continuum-fitting object {}'.format(indx))
    t0 = time.time()
    cfit, continuum = CFit.fnnls_continuum(data)
    log.info('Continuum-fitting object {} took {:.2f} sec'.format(indx, time.time()-t0))

    # fit the emission-line spectrum
    t0 = time.time()
    emfit = EMFit.fit(data, continuum)
    log.info('Line-fitting object {} took {:.2f} sec'.format(indx, time.time()-t0))

    for col in emfit.colnames:
        out[col] = emfit[col]
    for col in cfit.colnames:
        out[col] = cfit[col]
        
    return out

def parse(options=None):
    """Parse input arguments.

    """
    import argparse

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # required but with sensible defaults
    parser.add_argument('--night', default='20200225', type=str, help='Night to process.')
    parser.add_argument('--tile', default='70502', type=str, help='Tile number to process.')

    # optional inputs
    parser.add_argument('--first', type=int, help='Index of first spectrum to process (0-indexed).')
    parser.add_argument('--last', type=int, help='Index of last spectrum to process (max of nobj-1).')
    parser.add_argument('--nproc', default=1, type=int, help='Number of cores.')
    parser.add_argument('--use-vi', action='store_true', help='Select spectra with high-quality visual inspections (VI).')
    parser.add_argument('--overwrite', action='store_true', help='Overwrite any existing files.')
    parser.add_argument('--no-write-spectra', dest='write_spectra', default=True, action='store_false',
                        help='Do not write out the selected spectra for the specified tile and night.')
    parser.add_argument('--verbose', action='store_true', help='Be verbose.')

    log = get_logger()
    if options is None:
        args = parser.parse_args()
        log.info(' '.join(sys.argv))
    else:
        args = parser.parse_args(options)
        log.info('nyxgalaxy {}'.format(' '.join(options)))

    return args

def main(args=None):
    """Main module.

    """
    from astropy.table import vstack
    from desigal.nyxgalaxy import read_spectra, unpack_all_spectra, init_nyxgalaxy
    from desigal.nyxgalaxy import ContinuumFit, EMLineFit

    log = get_logger()
    if isinstance(args, (list, tuple, type(None))):
        args = parse(args)

    for key in ['NYXGALAXY_DATA', 'NYXGALAXY_TEMPLATES']:
        if key not in os.environ:
            log.fatal('Required ${} environment variable not set'.format(key))
            raise EnvironmentError('Required ${} environment variable not set'.format(key))

    nyxgalaxy_dir = os.getenv('NYXGALAXY_DATA')
    resultsdir = os.path.join(nyxgalaxy_dir, 'results')
    if not os.path.isdir(resultsdir):
        os.makedirs(resultsdir)

    # If the output file exists, we're done!
    nyxgalaxyfile = os.path.join(resultsdir, 'nyxgalaxy-{}-{}.fits'.format(
        args.tile, args.night))
    if os.path.isfile(nyxgalaxyfile) and not args.overwrite:
        log.info('Output file {} exists; all done!'.format(nyxgalaxyfile))
        return
        
    # Read the data 
    t0 = time.time()
    zbest, specobj = read_spectra(tile=args.tile, night=args.night,
                                  use_vi=args.use_vi, 
                                  write_spectra=args.write_spectra,
                                  verbose=args.verbose)
    log.info('Reading the data took: {:.2f} sec'.format(time.time()-t0))

    if args.first is None:
        args.first = 0
    if args.last is None:
        args.last = len(zbest) - 1
    if args.first > args.last:
        log.warning('Option --first cannot be larger than --last!')
        raise ValueError
    fitindx = np.arange(args.last - args.first + 1) + args.first

    # Initialize the continuum- and emission-line fitting classes and the output
    # data table.
    t0 = time.time()
    CFit = ContinuumFit(verbose=args.verbose)
    EMFit = EMLineFit(verbose=args.verbose)
    nyxgalaxy = init_nyxgalaxy(args.tile, args.night, zbest, specobj.fibermap, CFit, EMFit)
    log.info('Initializing the classes took: {:.2f} sec'.format(time.time()-t0))

    # Unpacking with multiprocessing takes a lot longer (maybe pickling takes a
    # long time?) so suppress the `nproc` argument here for now.
    t0 = time.time()
    data = unpack_all_spectra(specobj, zbest, CFit, fitindx)#, nproc=args.nproc)
    del specobj, zbest # free memory
    log.info('Unpacking the spectra to be fitted took: {:.2f} sec'.format(time.time()-t0))

    # Fit in parallel
    fitargs = [(indx, data[iobj], CFit, EMFit, nyxgalaxy[indx]) for iobj, indx in enumerate(fitindx)]
    if args.nproc > 1:
        with multiprocessing.Pool(args.nproc) as P:
            out = P.map(_nyxfit_one, fitargs)
    else:
        out = [nyxfit_one(*_fitargs) for _fitargs in fitargs]

    nyxgalaxy = vstack(out)

    #pdb.set_trace()
    #for iobj, indx in enumerate(fitindx):
    #    # fit the stellar continuum
    #    t0 = time.time()
    #    cfit, continuum = CFit.fnnls_continuum(data[iobj])
    #    log.info('Continuum-fitting object {} took {:.2f} sec'.format(indx, time.time()-t0))
    #
    #    # fit the emission-line spectrum
    #    t0 = time.time()
    #    emfit = EMFit.fit(data[iobj], continuum)
    #    log.info('Line-fitting object {} took {:.2f} sec'.format(indx, time.time()-t0))
    #
    #    for col in emfit.colnames:
    #        nyxgalaxy[col][indx] = emfit[col]
    #    for col in cfit.colnames:
    #        nyxgalaxy[col][indx] = cfit[col]

    # write out
    t0 = time.time()
    log.info('Writing results for {} objects to {}'.format(len(nyxgalaxy), nyxgalaxyfile))
    nyxgalaxy.write(nyxgalaxyfile, overwrite=True)
    log.info('Writing out took {:.2f} sec'.format(time.time()-t0))
