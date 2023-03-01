#!/usr/bin/env python

"""Each model will be written as a class here, instantiated and populated by
load.py, with each model stored as a table in the database and the fields stored
as columns.

"""
import os
import numpy as np
from django.db.models import Model, IntegerField, BigIntegerField, CharField, FloatField

# python manage.py makemigrations sample
# python manage.py migrate

class Sample(Model):
    """Model to represent a single object.

    """
    #def __str__(self):
    #    return 'Sample '+self.target_name
    
    # in FITS table
    row_index = BigIntegerField(default=0)#, db_index=True)

    # derived target name, e.g., sv3-bright-80613-TARGETID
    specprod = CharField(max_length=15, default='')
    target_name = CharField(max_length=40, default='')

    # for col in tt.colnames:
    #     if tt[col].dtype.name == 'float64':
    #         print('{} = FloatField(null=True)'.format(col.lower()))
    #     elif 'int' in tt[col].dtype.name:
    #         print('{} = IntegerField(null=True)'.format(col.lower()))

    # metadata columns
    #targetid = CharField(max_length=20, default='', db_index=True)
    targetid = BigIntegerField(null=True)#, db_index=True)
    survey = CharField(max_length=4, default='')#, db_index=True)
    program = CharField(max_length=6, default='')#, db_index=True)
    healpix = IntegerField(null=True)
    tileid_list = CharField(max_length=100, default='')
    #tileid = IntegerField(null=True)
    ra = FloatField(null=True)#, db_index=True)
    dec = FloatField(null=True)#, db_index=True)
    coadd_fiberstatus = CharField(max_length=20, default='')
    #fiber = IntegerField(null=True)

    cmx_target = CharField(max_length=20, default='')
    desi_target = CharField(max_length=20, default='')
    bgs_target = CharField(max_length=20, default='')
    mws_target = CharField(max_length=20, default='')
    sv1_desi_target = CharField(max_length=20, default='')
    sv1_bgs_target = CharField(max_length=20, default='')
    sv1_mws_target = CharField(max_length=20, default='')
    sv2_desi_target = CharField(max_length=20, default='')
    sv2_bgs_target = CharField(max_length=20, default='')
    sv2_mws_target = CharField(max_length=20, default='')
    sv3_desi_target = CharField(max_length=20, default='')
    sv3_bgs_target = CharField(max_length=20, default='')
    sv3_mws_target = CharField(max_length=20, default='')
    scnd_target = CharField(max_length=20, default='')
    sv1_scnd_target = CharField(max_length=20, default='')
    sv2_scnd_target = CharField(max_length=20, default='')
    sv3_scnd_target = CharField(max_length=20, default='')

    desi_bitnames = CharField(max_length=150, default='')
    bgs_bitnames = CharField(max_length=150, default='')
    mws_bitnames = CharField(max_length=150, default='')
    scnd_bitnames = CharField(max_length=150, default='')
    cmx_bitnames = CharField(max_length=150, default='')

    targetclass = CharField(max_length=150, default='')

    z = FloatField(null=True)#, db_index=True)
    zwarn = IntegerField(null=True)
    deltachi2 = FloatField(null=True)
    spectype = CharField(max_length=10, default='')
    zredrock = FloatField(null=True)
    tsnr2_bgs = FloatField(null=True)
    tsnr2_lrg = FloatField(null=True)
    tsnr2_elg = FloatField(null=True)
    tsnr2_qso = FloatField(null=True)
    tsnr2_lya = FloatField(null=True)

    photsys = CharField(max_length=1, default='')
    ebv = FloatField(null=True)
    mw_transmission_g = FloatField(null=True)
    mw_transmission_r = FloatField(null=True)
    mw_transmission_z = FloatField(null=True)
    mw_transmission_w1 = FloatField(null=True)
    mw_transmission_w2 = FloatField(null=True)
    mw_transmission_w3 = FloatField(null=True)
    mw_transmission_w4 = FloatField(null=True)
    fiberflux_g = FloatField(null=True)
    fiberflux_r = FloatField(null=True)
    fiberflux_z = FloatField(null=True)
    fibertotflux_g = FloatField(null=True)
    fibertotflux_r = FloatField(null=True)
    fibertotflux_z = FloatField(null=True)
    flux_g = FloatField(null=True)
    flux_r = FloatField(null=True)
    flux_z = FloatField(null=True)
    flux_w1 = FloatField(null=True)
    flux_w2 = FloatField(null=True)
    flux_w3 = FloatField(null=True)
    flux_w4 = FloatField(null=True)
    flux_ivar_g = FloatField(null=True)
    flux_ivar_r = FloatField(null=True)
    flux_ivar_z = FloatField(null=True)
    flux_ivar_w1 = FloatField(null=True)
    flux_ivar_w2 = FloatField(null=True)
    flux_ivar_w3 = FloatField(null=True)
    flux_ivar_w4 = FloatField(null=True)

    # continuum properties
    #continuum_z = FloatField(null=True)
    #coeff = FloatField(null=True)
    rchi2 = FloatField(null=True)
    rchi2_cont = FloatField(null=True)
    rchi2_phot = FloatField(null=True)
    snr_b = FloatField(null=True)
    snr_r = FloatField(null=True)
    snr_z = FloatField(null=True)
    smoothcorr_b = FloatField(null=True)
    smoothcorr_r = FloatField(null=True)
    smoothcorr_z = FloatField(null=True)
    
    vdisp = FloatField(null=True)
    vdisp_ivar = FloatField(null=True)
    vdisp_err = CharField(max_length=15, default='')
    
    age = FloatField(null=True)
    zzsun = FloatField(null=True)
    logmstar = FloatField(null=True)
    sfr = FloatField(null=True)
    #fagn = FloatField(null=True)
    av = FloatField(null=True)
    dn4000 = FloatField(null=True)
    dn4000_obs = FloatField(null=True)
    dn4000_ivar = FloatField(null=True)
    dn4000_model = FloatField(null=True)

    flux_synth_g = FloatField(null=True)
    flux_synth_r = FloatField(null=True)
    flux_synth_z = FloatField(null=True)
    flux_synth_specmodel_g = FloatField(null=True)
    flux_synth_specmodel_r = FloatField(null=True)
    flux_synth_specmodel_z = FloatField(null=True)
    flux_synth_photmodel_g = FloatField(null=True)
    flux_synth_photmodel_r = FloatField(null=True)
    flux_synth_photmodel_z = FloatField(null=True)
    flux_synth_photmodel_w1 = FloatField(null=True)
    flux_synth_photmodel_w2 = FloatField(null=True)
    flux_synth_photmodel_w3 = FloatField(null=True)
    flux_synth_photmodel_w4 = FloatField(null=True)

    kcorr_u = FloatField(null=True)
    kcorr_b = FloatField(null=True)
    kcorr_v = FloatField(null=True)
    kcorr_w1 = FloatField(null=True)
    kcorr_w2 = FloatField(null=True)
    absmag_u = FloatField(null=True)
    absmag_b = FloatField(null=True)
    absmag_v = FloatField(null=True)
    absmag_w1 = FloatField(null=True)
    absmag_w2 = FloatField(null=True)

    kcorr_sdss_u = FloatField(null=True)
    kcorr_sdss_g = FloatField(null=True)
    kcorr_sdss_r = FloatField(null=True)
    kcorr_sdss_i = FloatField(null=True)
    kcorr_sdss_z = FloatField(null=True)
    absmag_sdss_u = FloatField(null=True)
    absmag_sdss_g = FloatField(null=True)
    absmag_sdss_r = FloatField(null=True)
    absmag_sdss_i = FloatField(null=True)
    absmag_sdss_z = FloatField(null=True)

    abmag_g = CharField(max_length=15, default='')
    abmag_r = CharField(max_length=15, default='')
    abmag_z = CharField(max_length=15, default='')
    abmag_w1 = CharField(max_length=15, default='')
    abmag_w2 = CharField(max_length=15, default='')
    abmag_w3 = CharField(max_length=15, default='')
    abmag_w4 = CharField(max_length=15, default='')

    abmag_err_g = CharField(max_length=15, default='')
    abmag_err_r = CharField(max_length=15, default='')
    abmag_err_z = CharField(max_length=15, default='')
    abmag_err_w1 = CharField(max_length=15, default='')
    abmag_err_w2 = CharField(max_length=15, default='')
    abmag_err_w3 = CharField(max_length=15, default='')
    abmag_err_w4 = CharField(max_length=15, default='')

    fiberabmag_g = CharField(max_length=15, default='')
    fiberabmag_r = CharField(max_length=15, default='')
    fiberabmag_z = CharField(max_length=15, default='')

    fibertotabmag_g = CharField(max_length=15, default='')
    fibertotabmag_r = CharField(max_length=15, default='')
    fibertotabmag_z = CharField(max_length=15, default='')

    abmag_synth_g = CharField(max_length=15, default='')
    abmag_synth_r = CharField(max_length=15, default='')
    abmag_synth_z = CharField(max_length=15, default='')
    abmag_synth_specmodel_g = CharField(max_length=15, default='')
    abmag_synth_specmodel_r = CharField(max_length=15, default='')
    abmag_synth_specmodel_z = CharField(max_length=15, default='')
    abmag_synth_photmodel_g = CharField(max_length=15, default='')
    abmag_synth_photmodel_r = CharField(max_length=15, default='')
    abmag_synth_photmodel_z = CharField(max_length=15, default='')
    abmag_synth_photmodel_w1 = CharField(max_length=15, default='')
    abmag_synth_photmodel_w2 = CharField(max_length=15, default='')
    abmag_synth_photmodel_w3 = CharField(max_length=15, default='')
    abmag_synth_photmodel_w4 = CharField(max_length=15, default='')

    loglnu_1500 = FloatField(null=True)
    loglnu_2800 = FloatField(null=True)
    logl_5100 = FloatField(null=True)
    apercorr = FloatField(null=True)
    apercorr_g = FloatField(null=True)
    apercorr_r = FloatField(null=True)
    apercorr_z = FloatField(null=True)

    rchi2_line = FloatField(null=True)
    delta_linerchi2 = FloatField(null=True)

    narrow_z = FloatField(null=True)
    broad_z = FloatField(null=True)
    uv_z = FloatField(null=True)
    narrow_zrms = FloatField(null=True)
    broad_zrms = FloatField(null=True)
    uv_zrms = FloatField(null=True)
    narrow_dv = FloatField(null=True)
    broad_dv = FloatField(null=True)
    uv_dv = FloatField(null=True)
    narrow_dv_err = CharField(max_length=15, default='')    
    broad_dv_err = CharField(max_length=15, default='')    
    uv_dv_err = CharField(max_length=15, default='')    
    
    narrow_sigma = FloatField(null=True)
    broad_sigma = FloatField(null=True)
    uv_sigma = FloatField(null=True)
    narrow_sigmarms = FloatField(null=True)
    broad_sigmarms = FloatField(null=True)
    uv_sigmarms = FloatField(null=True)
    narrow_sigma_err = CharField(max_length=15, default='')    
    broad_sigma_err = CharField(max_length=15, default='')    
    uv_sigma_err = CharField(max_length=15, default='')    

    mgii_doublet_ratio = FloatField(null=True)
    oii_doublet_ratio = FloatField(null=True)
    sii_doublet_ratio = FloatField(null=True)

    lyalpha_wave = CharField(max_length=9, default='')
    oi_1304_wave = CharField(max_length=9, default='')
    siliv_1396_wave = CharField(max_length=9, default='')
    civ_1549_wave = CharField(max_length=9, default='')
    siliii_1892_wave = CharField(max_length=9, default='')
    ciii_1908_wave = CharField(max_length=9, default='')
    mgii_2796_wave = CharField(max_length=9, default='')
    mgii_2803_wave = CharField(max_length=9, default='')
    nev_3346_wave = CharField(max_length=9, default='')
    nev_3426_wave = CharField(max_length=9, default='')
    oii_3726_wave = CharField(max_length=9, default='')
    oii_3729_wave = CharField(max_length=9, default='')
    neiii_3869_wave = CharField(max_length=9, default='')
    #hei_3889_wave = CharField(max_length=9, default='')
    #hei_broad_3889_wave = CharField(max_length=9, default='')
    h6_wave = CharField(max_length=9, default='')
    h6_broad_wave = CharField(max_length=9, default='')
    hepsilon_wave = CharField(max_length=9, default='')
    hepsilon_broad_wave = CharField(max_length=9, default='')
    hdelta_wave = CharField(max_length=9, default='')
    hdelta_broad_wave = CharField(max_length=9, default='')
    hgamma_wave = CharField(max_length=9, default='')
    hgamma_broad_wave = CharField(max_length=9, default='')
    oiii_4363_wave = CharField(max_length=9, default='')
    hei_4471_wave = CharField(max_length=9, default='')
    hei_broad_4471_wave = CharField(max_length=9, default='')
    heii_4686_wave = CharField(max_length=9, default='')
    heii_broad_4686_wave = CharField(max_length=9, default='')
    hbeta_wave = CharField(max_length=9, default='')
    hbeta_broad_wave = CharField(max_length=9, default='')
    oiii_4959_wave = CharField(max_length=9, default='')
    oiii_5007_wave = CharField(max_length=9, default='')
    nii_5755_wave = CharField(max_length=9, default='')
    hei_5876_wave = CharField(max_length=9, default='')
    hei_broad_5876_wave = CharField(max_length=9, default='')
    oi_6300_wave = CharField(max_length=9, default='')
    siii_6312_wave = CharField(max_length=9, default='')
    nii_6548_wave = CharField(max_length=9, default='')
    halpha_wave = CharField(max_length=9, default='')
    halpha_broad_wave = CharField(max_length=9, default='')
    nii_6584_wave = CharField(max_length=9, default='')
    sii_6716_wave = CharField(max_length=9, default='')
    sii_6731_wave = CharField(max_length=9, default='')
    oii_7320_wave = CharField(max_length=9, default='')
    oii_7330_wave = CharField(max_length=9, default='')
    siii_9069_wave = CharField(max_length=9, default='')
    siii_9532_wave = CharField(max_length=9, default='')

    lyalpha_snr = CharField(max_length=15, default='')
    oi_1304_snr = CharField(max_length=15, default='')
    siliv_1396_snr = CharField(max_length=15, default='')
    civ_1549_snr = CharField(max_length=15, default='')
    siliii_1892_snr = CharField(max_length=15, default='')
    ciii_1908_snr = CharField(max_length=15, default='')
    mgii_2796_snr = CharField(max_length=15, default='')
    mgii_2803_snr = CharField(max_length=15, default='')
    nev_3346_snr = CharField(max_length=15, default='')
    nev_3426_snr = CharField(max_length=15, default='')
    oii_3726_snr = CharField(max_length=15, default='')
    oii_3729_snr = CharField(max_length=15, default='')
    neiii_3869_snr = CharField(max_length=15, default='')
    #hei_3889_snr = CharField(max_length=15, default='')
    #hei_broad_3889_snr = CharField(max_length=15, default='')
    h6_snr = CharField(max_length=15, default='')
    h6_broad_snr = CharField(max_length=15, default='')
    hepsilon_snr = CharField(max_length=15, default='')
    hepsilon_broad_snr = CharField(max_length=15, default='')
    hdelta_snr = CharField(max_length=15, default='')
    hdelta_broad_snr = CharField(max_length=15, default='')
    hgamma_snr = CharField(max_length=15, default='')
    hgamma_broad_snr = CharField(max_length=15, default='')
    oiii_4363_snr = CharField(max_length=15, default='')
    hei_4471_snr = CharField(max_length=15, default='')
    hei_broad_4471_snr = CharField(max_length=15, default='')
    heii_4686_snr = CharField(max_length=15, default='')
    heii_broad_4686_snr = CharField(max_length=15, default='')
    hbeta_snr = CharField(max_length=15, default='')
    hbeta_broad_snr = CharField(max_length=15, default='')
    oiii_4959_snr = CharField(max_length=15, default='')
    oiii_5007_snr = CharField(max_length=15, default='')
    nii_5755_snr = CharField(max_length=15, default='')
    hei_5876_snr = CharField(max_length=15, default='')
    hei_broad_5876_snr = CharField(max_length=15, default='')
    oi_6300_snr = CharField(max_length=15, default='')
    siii_6312_snr = CharField(max_length=15, default='')
    nii_6548_snr = CharField(max_length=15, default='')
    halpha_snr = CharField(max_length=15, default='')
    halpha_broad_snr = CharField(max_length=15, default='')
    nii_6584_snr = CharField(max_length=15, default='')
    sii_6716_snr = CharField(max_length=15, default='')
    sii_6731_snr = CharField(max_length=15, default='')
    oii_7320_snr = CharField(max_length=15, default='')
    oii_7330_snr = CharField(max_length=15, default='')
    siii_9069_snr = CharField(max_length=15, default='')
    siii_9532_snr = CharField(max_length=15, default='')

    lyalpha_vshift_str = CharField(max_length=15, default='')
    oi_1304_vshift_str = CharField(max_length=15, default='')
    siliv_1396_vshift_str = CharField(max_length=15, default='')
    civ_1549_vshift_str = CharField(max_length=15, default='')
    siliii_1892_vshift_str = CharField(max_length=15, default='')
    ciii_1908_vshift_str = CharField(max_length=15, default='')
    mgii_2796_vshift_str = CharField(max_length=15, default='')
    mgii_2803_vshift_str = CharField(max_length=15, default='')
    nev_3346_vshift_str = CharField(max_length=15, default='')
    nev_3426_vshift_str = CharField(max_length=15, default='')
    oii_3726_vshift_str = CharField(max_length=15, default='')
    oii_3729_vshift_str = CharField(max_length=15, default='')
    neiii_3869_vshift_str = CharField(max_length=15, default='')
    #hei_3889_vshift_str = CharField(max_length=15, default='')
    #hei_broad_3889_vshift_str = CharField(max_length=15, default='')
    h6_vshift_str = CharField(max_length=15, default='')
    h6_broad_vshift_str = CharField(max_length=15, default='')
    hepsilon_vshift_str = CharField(max_length=15, default='')
    hepsilon_broad_vshift_str = CharField(max_length=15, default='')
    hdelta_vshift_str = CharField(max_length=15, default='')
    hdelta_broad_vshift_str = CharField(max_length=15, default='')
    hgamma_vshift_str = CharField(max_length=15, default='')
    hgamma_broad_vshift_str = CharField(max_length=15, default='')
    oiii_4363_vshift_str = CharField(max_length=15, default='')
    hei_4471_vshift_str = CharField(max_length=15, default='')
    hei_broad_4471_vshift_str = CharField(max_length=15, default='')
    heii_4686_vshift_str = CharField(max_length=15, default='')
    heii_broad_4686_vshift_str = CharField(max_length=15, default='')
    hbeta_vshift_str = CharField(max_length=15, default='')
    hbeta_broad_vshift_str = CharField(max_length=15, default='')
    oiii_4959_vshift_str = CharField(max_length=15, default='')
    oiii_5007_vshift_str = CharField(max_length=15, default='')
    nii_5755_vshift_str = CharField(max_length=15, default='')
    hei_5876_vshift_str = CharField(max_length=15, default='')
    hei_broad_5876_vshift_str = CharField(max_length=15, default='')
    oi_6300_vshift_str = CharField(max_length=15, default='')
    siii_6312_vshift_str = CharField(max_length=15, default='')
    nii_6548_vshift_str = CharField(max_length=15, default='')
    halpha_vshift_str = CharField(max_length=15, default='')
    halpha_broad_vshift_str = CharField(max_length=15, default='')
    nii_6584_vshift_str = CharField(max_length=15, default='')
    sii_6716_vshift_str = CharField(max_length=15, default='')
    sii_6731_vshift_str = CharField(max_length=15, default='')
    oii_7320_vshift_str = CharField(max_length=15, default='')
    oii_7330_vshift_str = CharField(max_length=15, default='')
    siii_9069_vshift_str = CharField(max_length=15, default='')
    siii_9532_vshift_str = CharField(max_length=15, default='')

    lyalpha_sigma_str = CharField(max_length=15, default='')
    oi_1304_sigma_str = CharField(max_length=15, default='')
    siliv_1396_sigma_str = CharField(max_length=15, default='')
    civ_1549_sigma_str = CharField(max_length=15, default='')
    siliii_1892_sigma_str = CharField(max_length=15, default='')
    ciii_1908_sigma_str = CharField(max_length=15, default='')
    mgii_2796_sigma_str = CharField(max_length=15, default='')
    mgii_2803_sigma_str = CharField(max_length=15, default='')
    nev_3346_sigma_str = CharField(max_length=15, default='')
    nev_3426_sigma_str = CharField(max_length=15, default='')
    oii_3726_sigma_str = CharField(max_length=15, default='')
    oii_3729_sigma_str = CharField(max_length=15, default='')
    neiii_3869_sigma_str = CharField(max_length=15, default='')
    #hei_3889_sigma_str = CharField(max_length=15, default='')
    #hei_broad_3889_sigma_str = CharField(max_length=15, default='')
    h6_sigma_str = CharField(max_length=15, default='')
    h6_broad_sigma_str = CharField(max_length=15, default='')
    hepsilon_sigma_str = CharField(max_length=15, default='')
    hepsilon_broad_sigma_str = CharField(max_length=15, default='')
    hdelta_sigma_str = CharField(max_length=15, default='')
    hdelta_broad_sigma_str = CharField(max_length=15, default='')
    hgamma_sigma_str = CharField(max_length=15, default='')
    hgamma_broad_sigma_str = CharField(max_length=15, default='')
    oiii_4363_sigma_str = CharField(max_length=15, default='')
    hei_4471_sigma_str = CharField(max_length=15, default='')
    hei_broad_4471_sigma_str = CharField(max_length=15, default='')
    heii_4686_sigma_str = CharField(max_length=15, default='')
    heii_broad_4686_sigma_str = CharField(max_length=15, default='')
    hbeta_sigma_str = CharField(max_length=15, default='')
    hbeta_broad_sigma_str = CharField(max_length=15, default='')
    oiii_4959_sigma_str = CharField(max_length=15, default='')
    oiii_5007_sigma_str = CharField(max_length=15, default='')
    nii_5755_sigma_str = CharField(max_length=15, default='')
    hei_5876_sigma_str = CharField(max_length=15, default='')
    hei_broad_5876_sigma_str = CharField(max_length=15, default='')
    oi_6300_sigma_str = CharField(max_length=15, default='')
    siii_6312_sigma_str = CharField(max_length=15, default='')
    nii_6548_sigma_str = CharField(max_length=15, default='')
    halpha_sigma_str = CharField(max_length=15, default='')
    halpha_broad_sigma_str = CharField(max_length=15, default='')
    nii_6584_sigma_str = CharField(max_length=15, default='')
    sii_6716_sigma_str = CharField(max_length=15, default='')
    sii_6731_sigma_str = CharField(max_length=15, default='')
    oii_7320_sigma_str = CharField(max_length=15, default='')
    oii_7330_sigma_str = CharField(max_length=15, default='')
    siii_9069_sigma_str = CharField(max_length=15, default='')
    siii_9532_sigma_str = CharField(max_length=15, default='')

    lyalpha_chi2_str = CharField(max_length=15, default='')
    oi_1304_chi2_str = CharField(max_length=15, default='')
    siliv_1396_chi2_str = CharField(max_length=15, default='')
    civ_1549_chi2_str = CharField(max_length=15, default='')
    siliii_1892_chi2_str = CharField(max_length=15, default='')
    ciii_1908_chi2_str = CharField(max_length=15, default='')
    mgii_2796_chi2_str = CharField(max_length=15, default='')
    mgii_2803_chi2_str = CharField(max_length=15, default='')
    nev_3346_chi2_str = CharField(max_length=15, default='')
    nev_3426_chi2_str = CharField(max_length=15, default='')
    oii_3726_chi2_str = CharField(max_length=15, default='')
    oii_3729_chi2_str = CharField(max_length=15, default='')
    neiii_3869_chi2_str = CharField(max_length=15, default='')
    #hei_3889_chi2_str = CharField(max_length=15, default='')
    #hei_broad_3889_chi2_str = CharField(max_length=15, default='')
    h6_chi2_str = CharField(max_length=15, default='')
    h6_broad_chi2_str = CharField(max_length=15, default='')
    hepsilon_chi2_str = CharField(max_length=15, default='')
    hepsilon_broad_chi2_str = CharField(max_length=15, default='')
    hdelta_chi2_str = CharField(max_length=15, default='')
    hdelta_broad_chi2_str = CharField(max_length=15, default='')
    hgamma_chi2_str = CharField(max_length=15, default='')
    hgamma_broad_chi2_str = CharField(max_length=15, default='')
    oiii_4363_chi2_str = CharField(max_length=15, default='')
    hei_4471_chi2_str = CharField(max_length=15, default='')
    hei_broad_4471_chi2_str = CharField(max_length=15, default='')
    heii_4686_chi2_str = CharField(max_length=15, default='')
    heii_broad_4686_chi2_str = CharField(max_length=15, default='')
    hbeta_chi2_str = CharField(max_length=15, default='')
    hbeta_broad_chi2_str = CharField(max_length=15, default='')
    oiii_4959_chi2_str = CharField(max_length=15, default='')
    oiii_5007_chi2_str = CharField(max_length=15, default='')
    nii_5755_chi2_str = CharField(max_length=15, default='')
    hei_5876_chi2_str = CharField(max_length=15, default='')
    hei_broad_5876_chi2_str = CharField(max_length=15, default='')
    oi_6300_chi2_str = CharField(max_length=15, default='')
    siii_6312_chi2_str = CharField(max_length=15, default='')
    nii_6548_chi2_str = CharField(max_length=15, default='')
    halpha_chi2_str = CharField(max_length=15, default='')
    halpha_broad_chi2_str = CharField(max_length=15, default='')
    nii_6584_chi2_str = CharField(max_length=15, default='')
    sii_6716_chi2_str = CharField(max_length=15, default='')
    sii_6731_chi2_str = CharField(max_length=15, default='')
    oii_7320_chi2_str = CharField(max_length=15, default='')
    oii_7330_chi2_str = CharField(max_length=15, default='')
    siii_9069_chi2_str = CharField(max_length=15, default='')
    siii_9532_chi2_str = CharField(max_length=15, default='')

    lyalpha_npix = IntegerField(null=True)
    oi_1304_npix = IntegerField(null=True)
    siliv_1396_npix = IntegerField(null=True)
    civ_1549_npix = IntegerField(null=True)
    siliii_1892_npix = IntegerField(null=True)
    ciii_1908_npix = IntegerField(null=True)
    mgii_2796_npix = IntegerField(null=True)
    mgii_2803_npix = IntegerField(null=True)
    nev_3346_npix = IntegerField(null=True)
    nev_3426_npix = IntegerField(null=True)
    oii_3726_npix = IntegerField(null=True)
    oii_3729_npix = IntegerField(null=True)
    neiii_3869_npix = IntegerField(null=True)
    #hei_3889_npix = IntegerField(null=True)
    #hei_broad_3889_npix = IntegerField(null=True)
    h6_npix = IntegerField(null=True)
    h6_broad_npix = IntegerField(null=True)
    hepsilon_npix = IntegerField(null=True)
    hepsilon_broad_npix = IntegerField(null=True)
    hdelta_npix = IntegerField(null=True)
    hdelta_broad_npix = IntegerField(null=True)
    hgamma_npix = IntegerField(null=True)
    hgamma_broad_npix = IntegerField(null=True)
    oiii_4363_npix = IntegerField(null=True)
    hei_4471_npix = IntegerField(null=True)
    hei_broad_4471_npix = IntegerField(null=True)
    heii_4686_npix = IntegerField(null=True)
    heii_broad_4686_npix = IntegerField(null=True)
    hbeta_npix = IntegerField(null=True)
    hbeta_broad_npix = IntegerField(null=True)
    oiii_4959_npix = IntegerField(null=True)
    oiii_5007_npix = IntegerField(null=True)
    nii_5755_npix = IntegerField(null=True)
    hei_5876_npix = IntegerField(null=True)
    hei_broad_5876_npix = IntegerField(null=True)
    oi_6300_npix = IntegerField(null=True)
    siii_6312_npix = IntegerField(null=True)
    nii_6548_npix = IntegerField(null=True)
    halpha_npix = IntegerField(null=True)
    halpha_broad_npix = IntegerField(null=True)
    nii_6584_npix = IntegerField(null=True)
    sii_6716_npix = IntegerField(null=True)
    sii_6731_npix = IntegerField(null=True)
    oii_7320_npix = IntegerField(null=True)
    oii_7330_npix = IntegerField(null=True)
    siii_9069_npix = IntegerField(null=True)
    siii_9532_npix = IntegerField(null=True)

    lyalpha_amp_err = CharField(max_length=50, default='')
    lyalpha_flux_err = CharField(max_length=50, default='')
    lyalpha_cont_err = CharField(max_length=50, default='')
    lyalpha_ew_err = CharField(max_length=50, default='')
    oi_1304_amp_err = CharField(max_length=50, default='')
    oi_1304_flux_err = CharField(max_length=50, default='')
    oi_1304_cont_err = CharField(max_length=50, default='')
    oi_1304_ew_err = CharField(max_length=50, default='')
    siliv_1396_amp_err = CharField(max_length=50, default='')
    siliv_1396_flux_err = CharField(max_length=50, default='')
    siliv_1396_cont_err = CharField(max_length=50, default='')
    siliv_1396_ew_err = CharField(max_length=50, default='')
    civ_1549_amp_err = CharField(max_length=50, default='')
    civ_1549_flux_err = CharField(max_length=50, default='')
    civ_1549_cont_err = CharField(max_length=50, default='')
    civ_1549_ew_err = CharField(max_length=50, default='')
    siliii_1892_amp_err = CharField(max_length=50, default='')
    siliii_1892_flux_err = CharField(max_length=50, default='')
    siliii_1892_cont_err = CharField(max_length=50, default='')
    siliii_1892_ew_err = CharField(max_length=50, default='')
    ciii_1908_amp_err = CharField(max_length=50, default='')
    ciii_1908_flux_err = CharField(max_length=50, default='')
    ciii_1908_cont_err = CharField(max_length=50, default='')
    ciii_1908_ew_err = CharField(max_length=50, default='')
    mgii_2796_amp_err = CharField(max_length=50, default='')
    mgii_2796_flux_err = CharField(max_length=50, default='')
    mgii_2796_cont_err = CharField(max_length=50, default='')
    mgii_2796_ew_err = CharField(max_length=50, default='')
    mgii_2803_amp_err = CharField(max_length=50, default='')
    mgii_2803_flux_err = CharField(max_length=50, default='')
    mgii_2803_cont_err = CharField(max_length=50, default='')
    mgii_2803_ew_err = CharField(max_length=50, default='')
    nev_3346_amp_err = CharField(max_length=50, default='')
    nev_3346_flux_err = CharField(max_length=50, default='')
    nev_3346_cont_err = CharField(max_length=50, default='')
    nev_3346_ew_err = CharField(max_length=50, default='')
    nev_3426_amp_err = CharField(max_length=50, default='')
    nev_3426_flux_err = CharField(max_length=50, default='')
    nev_3426_cont_err = CharField(max_length=50, default='')
    nev_3426_ew_err = CharField(max_length=50, default='')
    oii_3726_amp_err = CharField(max_length=50, default='')
    oii_3726_flux_err = CharField(max_length=50, default='')
    oii_3726_cont_err = CharField(max_length=50, default='')
    oii_3726_ew_err = CharField(max_length=50, default='')
    oii_3729_amp_err = CharField(max_length=50, default='')
    oii_3729_flux_err = CharField(max_length=50, default='')
    oii_3729_cont_err = CharField(max_length=50, default='')
    oii_3729_ew_err = CharField(max_length=50, default='')
    neiii_3869_amp_err = CharField(max_length=50, default='')
    neiii_3869_flux_err = CharField(max_length=50, default='')
    neiii_3869_cont_err = CharField(max_length=50, default='')
    neiii_3869_ew_err = CharField(max_length=50, default='')
    #hei_3889_amp_err = CharField(max_length=50, default='')
    #hei_3889_flux_err = CharField(max_length=50, default='')
    #hei_3889_cont_err = CharField(max_length=50, default='')
    #hei_3889_ew_err = CharField(max_length=50, default='')
    #hei_broad_3889_amp_err = CharField(max_length=50, default='')
    #hei_broad_3889_flux_err = CharField(max_length=50, default='')
    #hei_broad_3889_cont_err = CharField(max_length=50, default='')
    #hei_broad_3889_ew_err = CharField(max_length=50, default='')
    h6_amp_err = CharField(max_length=50, default='')
    h6_flux_err = CharField(max_length=50, default='')
    h6_cont_err = CharField(max_length=50, default='')
    h6_ew_err = CharField(max_length=50, default='')
    h6_broad_amp_err = CharField(max_length=50, default='')
    h6_broad_flux_err = CharField(max_length=50, default='')
    h6_broad_cont_err = CharField(max_length=50, default='')
    h6_broad_ew_err = CharField(max_length=50, default='')
    hepsilon_amp_err = CharField(max_length=50, default='')
    hepsilon_flux_err = CharField(max_length=50, default='')
    hepsilon_cont_err = CharField(max_length=50, default='')
    hepsilon_ew_err = CharField(max_length=50, default='')
    hepsilon_broad_amp_err = CharField(max_length=50, default='')
    hepsilon_broad_flux_err = CharField(max_length=50, default='')
    hepsilon_broad_cont_err = CharField(max_length=50, default='')
    hepsilon_broad_ew_err = CharField(max_length=50, default='')
    hdelta_amp_err = CharField(max_length=50, default='')
    hdelta_flux_err = CharField(max_length=50, default='')
    hdelta_cont_err = CharField(max_length=50, default='')
    hdelta_ew_err = CharField(max_length=50, default='')
    hdelta_broad_amp_err = CharField(max_length=50, default='')
    hdelta_broad_flux_err = CharField(max_length=50, default='')
    hdelta_broad_cont_err = CharField(max_length=50, default='')
    hdelta_broad_ew_err = CharField(max_length=50, default='')
    hgamma_amp_err = CharField(max_length=50, default='')
    hgamma_flux_err = CharField(max_length=50, default='')
    hgamma_cont_err = CharField(max_length=50, default='')
    hgamma_ew_err = CharField(max_length=50, default='')
    hgamma_broad_amp_err = CharField(max_length=50, default='')
    hgamma_broad_flux_err = CharField(max_length=50, default='')
    hgamma_broad_cont_err = CharField(max_length=50, default='')
    hgamma_broad_ew_err = CharField(max_length=50, default='')
    oiii_4363_amp_err = CharField(max_length=50, default='')
    oiii_4363_flux_err = CharField(max_length=50, default='')
    oiii_4363_cont_err = CharField(max_length=50, default='')
    oiii_4363_ew_err = CharField(max_length=50, default='')
    hei_4471_amp_err = CharField(max_length=50, default='')
    hei_4471_flux_err = CharField(max_length=50, default='')
    hei_4471_cont_err = CharField(max_length=50, default='')
    hei_4471_ew_err = CharField(max_length=50, default='')
    hei_broad_4471_amp_err = CharField(max_length=50, default='')
    hei_broad_4471_flux_err = CharField(max_length=50, default='')
    hei_broad_4471_cont_err = CharField(max_length=50, default='')
    hei_broad_4471_ew_err = CharField(max_length=50, default='')
    heii_4686_amp_err = CharField(max_length=50, default='')
    heii_4686_flux_err = CharField(max_length=50, default='')
    heii_4686_cont_err = CharField(max_length=50, default='')
    heii_4686_ew_err = CharField(max_length=50, default='')
    heii_broad_4686_amp_err = CharField(max_length=50, default='')
    heii_broad_4686_flux_err = CharField(max_length=50, default='')
    heii_broad_4686_cont_err = CharField(max_length=50, default='')
    heii_broad_4686_ew_err = CharField(max_length=50, default='')
    hbeta_amp_err = CharField(max_length=50, default='')
    hbeta_flux_err = CharField(max_length=50, default='')
    hbeta_cont_err = CharField(max_length=50, default='')
    hbeta_ew_err = CharField(max_length=50, default='')
    hbeta_broad_amp_err = CharField(max_length=50, default='')
    hbeta_broad_flux_err = CharField(max_length=50, default='')
    hbeta_broad_cont_err = CharField(max_length=50, default='')
    hbeta_broad_ew_err = CharField(max_length=50, default='')
    oiii_4959_amp_err = CharField(max_length=50, default='')
    oiii_4959_flux_err = CharField(max_length=50, default='')
    oiii_4959_cont_err = CharField(max_length=50, default='')
    oiii_4959_ew_err = CharField(max_length=50, default='')
    oiii_5007_amp_err = CharField(max_length=50, default='')
    oiii_5007_flux_err = CharField(max_length=50, default='')
    oiii_5007_cont_err = CharField(max_length=50, default='')
    oiii_5007_ew_err = CharField(max_length=50, default='')
    nii_5755_amp_err = CharField(max_length=50, default='')
    nii_5755_flux_err = CharField(max_length=50, default='')
    nii_5755_cont_err = CharField(max_length=50, default='')
    nii_5755_ew_err = CharField(max_length=50, default='')
    hei_5876_amp_err = CharField(max_length=50, default='')
    hei_5876_flux_err = CharField(max_length=50, default='')
    hei_5876_cont_err = CharField(max_length=50, default='')
    hei_5876_ew_err = CharField(max_length=50, default='')
    hei_broad_5876_amp_err = CharField(max_length=50, default='')
    hei_broad_5876_flux_err = CharField(max_length=50, default='')
    hei_broad_5876_cont_err = CharField(max_length=50, default='')
    hei_broad_5876_ew_err = CharField(max_length=50, default='')
    oi_6300_amp_err = CharField(max_length=50, default='')
    oi_6300_flux_err = CharField(max_length=50, default='')
    oi_6300_cont_err = CharField(max_length=50, default='')
    oi_6300_ew_err = CharField(max_length=50, default='')
    siii_6312_amp_err = CharField(max_length=50, default='')
    siii_6312_flux_err = CharField(max_length=50, default='')
    siii_6312_cont_err = CharField(max_length=50, default='')
    siii_6312_ew_err = CharField(max_length=50, default='')
    nii_6548_amp_err = CharField(max_length=50, default='')
    nii_6548_flux_err = CharField(max_length=50, default='')
    nii_6548_cont_err = CharField(max_length=50, default='')
    nii_6548_ew_err = CharField(max_length=50, default='')
    halpha_amp_err = CharField(max_length=50, default='')
    halpha_flux_err = CharField(max_length=50, default='')
    halpha_cont_err = CharField(max_length=50, default='')
    halpha_ew_err = CharField(max_length=50, default='')
    halpha_broad_amp_err = CharField(max_length=50, default='')
    halpha_broad_flux_err = CharField(max_length=50, default='')
    halpha_broad_cont_err = CharField(max_length=50, default='')
    halpha_broad_ew_err = CharField(max_length=50, default='')
    nii_6584_amp_err = CharField(max_length=50, default='')
    nii_6584_flux_err = CharField(max_length=50, default='')
    nii_6584_cont_err = CharField(max_length=50, default='')
    nii_6584_ew_err = CharField(max_length=50, default='')
    sii_6716_amp_err = CharField(max_length=50, default='')
    sii_6716_flux_err = CharField(max_length=50, default='')
    sii_6716_cont_err = CharField(max_length=50, default='')
    sii_6716_ew_err = CharField(max_length=50, default='')
    sii_6731_amp_err = CharField(max_length=50, default='')
    sii_6731_flux_err = CharField(max_length=50, default='')
    sii_6731_cont_err = CharField(max_length=50, default='')
    sii_6731_ew_err = CharField(max_length=50, default='')
    oii_7320_amp_err = CharField(max_length=50, default='')
    oii_7320_flux_err = CharField(max_length=50, default='')
    oii_7320_cont_err = CharField(max_length=50, default='')
    oii_7320_ew_err = CharField(max_length=50, default='')
    oii_7330_amp_err = CharField(max_length=50, default='')
    oii_7330_flux_err = CharField(max_length=50, default='')
    oii_7330_cont_err = CharField(max_length=50, default='')
    oii_7330_ew_err = CharField(max_length=50, default='')
    siii_9069_amp_err = CharField(max_length=50, default='')
    siii_9069_flux_err = CharField(max_length=50, default='')
    siii_9069_cont_err = CharField(max_length=50, default='')
    siii_9069_ew_err = CharField(max_length=50, default='')
    siii_9532_amp_err = CharField(max_length=50, default='')
    siii_9532_flux_err = CharField(max_length=50, default='')
    siii_9532_cont_err = CharField(max_length=50, default='')
    siii_9532_ew_err = CharField(max_length=50, default='')

    # radec2xyz, for cone search in the database
    ux = FloatField(default=-2.0)
    uy = FloatField(default=-2.0)
    uz = FloatField(default=-2.0)

    def str_healpix(self):
        return str(self.healpix)

    def str_targetid(self):
        return str(self.targetid)

    def base_html_dir(self):
        # Hack!
        #return '/global/cfs/cdirs/desi/spectro/fastspecfit/fuji-webapp-test/html/'
        #return '/global/cfs/cdirs/desi/spectro/fastspecfit/fuji-webapp-test/{}/html/'.format(self.specprod)
        return '/global/cfs/cdirs/desi/spectro/fastspecfit/{}/html/'.format(specprod)

    def png_base_url(self):
        # different for cumulative coadds!
        # /data is mounted to /global/cfs/cdirs/desi/spectro/fastspecfit in the Spin server configuration
        # Hack!
        #baseurl = '/data/fuji-webapp-test/html/tiles/cumulative/{}/'.format(self.tileid_list)
        baseurl = '/data/{}/html/healpix/{}/{}/'.format(self.specprod, self.survey, self.program)
        baseurl += str(int(self.healpix)//100) +'/'+ self.str_healpix()
        return baseurl

    def data_base_url(self):
        # different for cumulative coadds!
        #baseurl = 'https://data.desi.lbl.gov/desi/spectro/fastspecfit/fuji-webapp-test/tiles/cumulative/{}/'.format(self.tileid_list) # no html subdir
        baseurl = 'https://data.desi.lbl.gov/desi/spectro/fastspecfit/{}/healpix/{}/{}/'.format(self.specprod, self.survey, self.program) # no html subdir
        baseurl += str(int(self.healpix)//100) +'/'+ self.str_healpix()
        return baseurl
