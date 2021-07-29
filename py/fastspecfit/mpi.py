"""
fastspecfit.mpi
===============

MPI tools.

"""
import pdb # for debuggin

import os, time
import numpy as np
from glob import glob

from desiutil.log import get_logger
log = get_logger()

def weighted_partition(weights, n):
    '''
    Partition `weights` into `n` groups with approximately same sum(weights)

    Args:
        weights: array-like weights
        n: number of groups

    Returns (groups, groupweights):
        * groups: list of lists of indices of weights for each group
        * groupweights: sum of weights assigned to each group

    Notes:
        similar to `redrock.utils.distribute_work`, which was written
            independently; these have not yet been compared.
        within each group, the weights are sorted largest to smallest
    '''
    sumweights = np.zeros(n, dtype=float)
    groups = list()
    for i in range(n):
        groups.append(list())
    weights = np.asarray(weights)
    for i in np.argsort(-weights):
        j = np.argmin(sumweights)
        groups[j].append(i)
        sumweights[j] += weights[i]

    return groups, np.array([np.sum(x) for x in sumweights])

def group_redrockfiles(specfiles, maxnodes=256, comm=None, makeqa=False):
    '''
    Group redrockfiles to balance runtimes

    Args:
        specfiles: list of spectra filepaths

    Options:
        maxnodes: split the spectra into this number of nodes
        comm: MPI communicator

    Returns (groups, ntargets, grouptimes):
      * groups: list of lists of indices to specfiles
      * list of number of targets per group
      * grouptimes: list of expected runtimes for each group

    '''
    import fitsio
    
    if comm is None:
        rank, size = 0, 1
    else:
        rank, size = comm.rank, comm.size

    npix = len(specfiles)
    pixgroups = np.array_split(np.arange(npix), size)
    ntargets = np.zeros(len(pixgroups[rank]), dtype=int)
    for i, j in enumerate(pixgroups[rank]):
        if makeqa:
            ntargets[i] = fitsio.FITS(specfiles[j])[1].get_nrows()
        else:
            zb = fitsio.read(specfiles[j], 'REDSHIFTS', columns=['Z', 'ZWARN', 'TARGETID'])
            fm = fitsio.read(specfiles[j], 'FIBERMAP', columns=['OBJTYPE', 'COADD_FIBERSTATUS', 'TARGETID'])
            _, I, _ = np.intersect1d(fm['TARGETID'], zb['TARGETID'], return_indices=True)
            fm = fm[I]
            assert(np.all(zb['TARGETID'] == fm['TARGETID']))
            J = ((zb['Z'] > 0) * (zb['ZWARN'] == 0) * #(zb['SPECTYPE'] == 'GALAXY') * 
                 (fm['OBJTYPE'] == 'TGT') * (fm['COADD_FIBERSTATUS'] == 0))
            ntargets[i] = np.count_nonzero(J)

    if comm is not None:
        ntargets = comm.gather(ntargets)
        if rank == 0:
            ntargets = np.concatenate(ntargets)
        ntargets = comm.bcast(ntargets, root=0)

    runtimes = 30 + 0.4*ntargets

    # Aim for 25 minutes, but don't exceed maxnodes number of nodes.
    ntime = 25
    if comm is not None:
        numnodes = comm.size
    else:
        numnodes = min(maxnodes, int(np.ceil(np.sum(runtimes)/(ntime*60))))

    groups, grouptimes = weighted_partition(runtimes, numnodes)
    ntargets = np.array([np.sum(ntargets[ii]) for ii in groups])
    return groups, ntargets, grouptimes

def backup_logs(logfile):
    '''
    Move logfile -> logfile.0 or logfile.1 or logfile.n as needed

    TODO: make robust against logfile.abc also existing
    '''
    logfiles = glob(logfile+'.*')
    newlog = logfile+'.'+str(len(logfiles))
    assert not os.path.exists(newlog)
    os.rename(logfile, newlog)
    return newlog

def plan(args, comm=None, merge=False, makeqa=False, fastphot=False,
         specprod_dir=None, base_datadir='.', base_htmldir='.'):

    import fitsio
    from astropy.table import Table, vstack
    from fastspecfit.io import DESI_ROOT_NERSC

    t0 = time.time()
    if comm is None:
        rank, size = 0, 1
    else:
        rank, size = comm.rank, comm.size

    if fastphot:
        outprefix = 'fastphot'
    else:
        outprefix = 'fastspec'

    if rank == 0:
        desi_root = os.environ.get('DESI_ROOT', DESI_ROOT_NERSC)
        # look for data in the standard location
        if specprod_dir is None:
            specprod_dir = os.path.join(desi_root, 'spectro', 'redux', args.specprod, 'tiles')

        # figure out which tiles belong to the SV programs
        if args.tile is None:
            tilefile = os.path.join(desi_root, 'spectro', 'redux', args.specprod, 'tiles-{}.csv'.format(args.specprod))
            alltileinfo = Table.read(tilefile)
            tileinfo = alltileinfo[['sv' in survey for survey in alltileinfo['SURVEY']]]
            #tileinfo = tileinfo[['sv' in survey or 'cmx' in survey for survey in tileinfo['SURVEY']]]

            #log.info('Add tiles 80605-80610 which are incorrectly identified as cmx tiles.')
            #tileinfo = vstack((tileinfo, alltileinfo[np.where((alltileinfo['TILEID'] >= 80605) * (alltileinfo['TILEID'] <= 80610))[0]]))
            #tileinfo = tileinfo[np.argsort(tileinfo['TILEID'])]

            log.info('Retrieved a list of {} {} tiles from {}'.format(
                len(tileinfo), ','.join(sorted(set(tileinfo['SURVEY']))), tilefile))

            # old 
            #tilefile = '/global/cfs/cdirs/desi/survey/observations/SV1/sv1-tiles.fits'
            #tileinfo = fitsio.read(tilefile)#, columns='PROGRAM')
            #tileinfo = tileinfo[tileinfo['PROGRAM'] == 'SV1']
            #log.info('Retrieved a list of {} SV1 tiles from {}'.format(len(tileinfo), tilefile))

            #alltiles = np.array(list(set(tileinfo['TILEID'])))
            #ireduced = [os.path.isdir(os.path.join(specprod_dir, args.coadd_type, str(tile1))) for tile1 in alltiles]
            #log.info('In specprod={}, {}/{} of these tiles have been reduced.'.format(
            #    args.specprod, np.sum(ireduced), len(alltiles)))
            #args.tile = alltiles[ireduced]
            #tileinfo = tileinfo[ireduced]

            args.tile = np.array(list(set(tileinfo['TILEID'])))
            #print(args.tile)

            #if True:
            #    tileinfo = tileinfo[['lrg' in program or 'elg' in program for program in tileinfo['FAPRGRM']]]
            #    args.tile = np.array(list(set(tileinfo['TILEID'])))
            #print(tileinfo)

        outdir = os.path.join(base_datadir, args.specprod, 'tiles')
        htmldir = os.path.join(base_htmldir, args.specprod, 'tiles')

        def _findfiles(filedir, prefix='redrock'):
            if args.coadd_type == 'cumulative':
                if args.tile is not None:
                    thesefiles = np.array(sorted(set(np.hstack([glob(os.path.join(
                        filedir, 'cumulative', str(tile), '????????', '{}-[0-9]-{}-thru????????.fits'.format(
                        prefix, tile))) for tile in args.tile]))))
                else:
                    thesefiles = np.array(sorted(set(glob(os.path.join(
                        filedir, 'cumulative', '?????', '????????', '{}-[0-9]-?????-thru????????.fits'.format(prefix))))))
            elif args.coadd_type == 'pernight':
                if args.tile is not None and args.night is not None:
                    thesefiles = []
                    for tile in args.tile:
                        for night in args.night:
                            thesefiles.append(glob(os.path.join(
                                filedir, 'pernight', str(tile), str(night), '{}-[0-9]-{}-{}.fits'.format(prefix, tile, night))))
                    thesefiles = np.array(sorted(set(np.hstack(thesefiles))))
                elif args.tile is not None and args.night is None:
                    thesefiles = np.array(sorted(set(np.hstack([glob(os.path.join(
                        filedir, 'pernight', str(tile), '????????', '{}-[0-9]-{}-????????.fits'.format(
                        prefix, tile))) for tile in args.tile]))))
                elif args.tile is None and args.night is not None:
                    thesefiles = np.array(sorted(set(np.hstack([glob(os.path.join(
                        filedir, 'pernight', '?????', str(night), '{}-[0-9]-?????-{}.fits'.format(
                        prefix, night))) for night in args.night]))))
                else:
                    thesefiles = np.array(sorted(set(glob(os.path.join(
                        filedir, '?????', '????????', '{}-[0-9]-?????-????????.fits'.format(prefix))))))
            elif args.coadd_type == 'perexp':
                if args.tile is not None:
                    thesefiles = np.array(sorted(set(np.hstack([glob(os.path.join(
                        filedir, 'perexp', str(tile), '????????', '{}-[0-9]-{}-exp????????.fits'.format(
                        prefix, tile))) for tile in args.tile]))))
                else:
                    thesefiles = np.array(sorted(set(glob(os.path.join(
                        filedir, 'perexp', '?????', '????????', '{}-[0-9]-?????-exp????????.fits'.format(prefix))))))
            else:
                pass
            return thesefiles

        if args.merge:
            redrockfiles = None
            outfiles = _findfiles(outdir, prefix=outprefix)
            log.info('Found {} {} files to be merged.'.format(len(outfiles), outprefix))
        elif args.makeqa:
            redrockfiles = None
            outfiles = _findfiles(outdir, prefix=outprefix)
            log.info('Found {} {} files for QA.'.format(len(outfiles), outprefix))
        else:
            redrockfiles = _findfiles(specprod_dir, prefix='redrock')
            nfile = len(redrockfiles)

            outfiles = np.array([redrockfile.replace(specprod_dir, outdir).replace('redrock-', '{}-'.format(outprefix)) for redrockfile in redrockfiles])
            todo = np.ones(len(redrockfiles), bool)
            for ii, outfile in enumerate(outfiles):
                if os.path.isfile(outfile) and not args.overwrite:
                    todo[ii] = False
            redrockfiles = redrockfiles[todo]
            outfiles = outfiles[todo]

            log.info('Found {}/{} redrockfiles (left) to do.'.format(len(redrockfiles), nfile))
    else:
        outdir = None
        redrockfiles = None
        outfiles = None

    if comm:
        outdir = comm.bcast(outdir, root=0)
        redrockfiles = comm.bcast(redrockfiles, root=0)
        outfiles = comm.bcast(outfiles, root=0)

    if args.merge:
        if len(outfiles) == 0:
            if rank == 0:
                log.info('No {} files in {} found!'.format(outprefix, outdir))
            return '', list(), list(), list(), list()
        return outdir, redrockfiles, outfiles, None, None
    elif args.makeqa:
        if len(outfiles) == 0:
            if rank == 0:
                log.info('No {} files in {} found!'.format(outprefix, outdir))
            return '', list(), list(), list(), list()
        #  hack--build the output directories and pass them in the 'redrockfiles'
        #  position! for coadd_type==cumulative, strip out the 'lastnight' argument
        if args.coadd_type == 'cumulative':
            #redrockfiles = []
            #for outfile in outfiles:
            #    dd = os.path.split(outfile)
            #    redrockfiles.append(os.path.dirname(dd[0]).replace(outdir, htmldir))
            #    os.path.dirname(dd[0])
            redrockfiles = np.array([os.path.dirname(os.path.dirname(outfile)).replace(outdir, htmldir) for outfile in outfiles])
        else:
            redrockfiles = np.array([os.path.dirname(outfile).replace(outdir, htmldir) for outfile in outfiles])
    else:
        if len(redrockfiles) == 0:
            if rank == 0:
                log.info('All files have been processed!')
            return '', list(), list(), list(), list()

    if args.makeqa:
        groups, ntargets, grouptimes = group_redrockfiles(outfiles, args.maxnodes, comm=comm, makeqa=True)
    else:
        groups, ntargets, grouptimes = group_redrockfiles(redrockfiles, args.maxnodes, comm=comm)

    if args.plan and rank == 0:
        plantime = time.time() - t0
        if plantime + np.max(grouptimes) <= (30*60):
            queue = 'debug'
        else:
            queue = 'regular'

        numnodes = len(groups)

        if os.getenv('NERSC_HOST') == 'cori':
            maxproc = 64
        else:
            maxproc = 8

        if args.mp is None:
            args.mp = maxproc // 2

        #- scale longer if purposefullying using fewer cores (e.g. for memory)
        if args.mp < maxproc // 2:
            scale = (maxproc//2) / args.mp
            grouptimes *= scale

        jobtime = int(1.15 * (plantime + np.max(grouptimes)))
        jobhours = jobtime // 3600
        jobminutes = (jobtime - jobhours*3600) // 60
        jobseconds = jobtime - jobhours*3600 - jobminutes*60

        print('#!/bin/bash')
        print('#SBATCH -N {}'.format(numnodes))
        print('#SBATCH -q {}'.format(queue))
        print('#SBATCH -J fastphot')
        if os.getenv('NERSC_HOST') == 'cori':
            print('#SBATCH -C haswell')
        print('#SBATCH -t {:02d}:{:02d}:{:02d}'.format(jobhours, jobminutes, jobseconds))
        print()
        print('# {} pixels with {} targets'.format(len(redrockfiles), np.sum(ntargets)))
        ### print('# plan time {:.1f} minutes'.format(plantime / 60))
        print('# Using {} nodes in {} queue'.format(numnodes, queue))
        print('# expected rank runtimes ({:.1f}, {:.1f}, {:.1f}) min/mid/max minutes'.format(
            np.min(grouptimes)/60, np.median(grouptimes)/60, np.max(grouptimes)/60
        ))
        ibiggest = np.argmax(grouptimes)
        print('# Largest node has {} specfile(s) with {} total targets'.format(
            len(groups[ibiggest]), ntargets[ibiggest]))

        print()
        print('export OMP_NUM_THREADS=1')
        print('unset OMP_PLACES')
        print('unset OMP_PROC_BIND')
        print('export MPICH_GNI_FORK_MODE=FULLCOPY')
        print()
        print('nodes=$SLURM_JOB_NUM_NODES')
        if False:
            rrcmd = '{} --mp {} --reduxdir {}'.format(
                os.path.abspath(__file__), args.mp, args.reduxdir)
            if args.outdir is not None:
                rrcmd += ' --outdir {}'.format(os.path.abspath(args.outdir))
            print('srun -N $nodes -n $nodes -c {} {}'.format(maxproc, rrcmd))

    return outdir, redrockfiles, outfiles, groups, grouptimes

def merge_fastspecfit(args, fastphot=False, specprod_dir=None):
    """Merge all the individual catalogs into a single large catalog. Runs only on
    rank 0.

    """
    import fitsio
    from astropy.io import fits
    from astropy.table import Table, vstack
    from fastspecfit.mpi import plan
    from fastspecfit.io import write_fastspecfit

    if fastphot:
        outprefix = 'fastphot'
        extname = 'FASTPHOT'
    else:
        outprefix = 'fastspec'
        extname = 'FASTSPEC'

    outdir, _, outfiles, _, _ = plan(args, merge=True, fastphot=fastphot,
                                     specprod_dir=specprod_dir)

    mergedir = os.path.join(outdir, 'merged')
    if not os.path.isdir(mergedir):
        os.makedirs(mergedir, exist_ok=True)

    #if args.coadd_type == 'deep-coadds':
    #    mergeprefix = 'deep'
    #elif args.coadd_type == 'night-coadds':
    #    mergeprefix = ''
    #elif args.coadd_type == 'night-coadds':

    mergefile = os.path.join(mergedir, '{}-{}-{}.fits'.format(outprefix, args.specprod, args.coadd_type))
    if os.path.isfile(mergefile) and not args.overwrite:
        log.info('Merged output file {} exists!'.format(mergefile))
        return

    t0 = time.time()
    out, meta = [], []
    for outfile in outfiles:
        out.append(Table(fitsio.read(outfile, ext=extname)))
        meta.append(Table(fitsio.read(outfile, ext='METADATA')))
    out = vstack(out)
    meta = vstack(meta)
    log.info('Merging {} objects from {} {} files took {:.2f} min.'.format(
        len(out), len(outfiles), outprefix, (time.time()-t0)/60.0))

    write_fastspecfit(out, meta, outfile=mergefile, specprod=args.specprod,
                      coadd_type=args.coadd_type, fastphot=fastphot)
