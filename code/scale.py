# default is 5 unless otherwise specified (0-4 scale)
question_scales = {
    'v2caconmob': 4,    
    'v2clgeocl':6,
    'v2clkill':6,
    'v2clpolcl':6,
    'v2csgender':6,
    'v2cademmob':6,
    'v2dlencmps':6,
    'v2csrlgrep':6,
    'v2dlcommon':6,
    'v2elaccept':6,
    'v2elembcap':6,
    'v2clprptym':6,
    'v2clprptyw':6,
    'v2clrgunev':3, 
    'v2cscnsult':3,
    'v2csprtcpt':4,
    'v2csrlgcon': 3,
    'v2dlconslt': 6,
    'v2dlcountr':6,
    'v2dlengage':6,
    'v2dlunivl':6,
    'v2edcentcurrlm': 4,
    'v2edcenttxbooks': 3,
    'v2edcritical':4,
    'v2edideol': 4,
    'v2edpatriot':4,
    'v2edplural':4,
    'v2edpoledrights': 4,
    'v2edscextracurr': 3,
    'v2edscpatriotcb': 4,
    'v2edteautonomy:': 4,
    'v2edtefire':4,
    'v2edtehire':4,
    'v2edtequal':4,
    'v2edteunionindp':4,
    'v2elasmoff':3,
    'v2elfrcamp':3,
    'v2elpaidig':4,
    'v2elpdcamp':4,
    'v2elsnlsff':3,
    'v2exdfcbhs_rec':3,
    'v2exdfdmhs':4,
    'v2exdfdshg':4,
    'v2exdfdshs':4,
    'v2exdfpphg':3,
    'v2exdfpphs':3,
    'v2exdjcbhg':3, 
    'v2exdjdshg':4, 
    'v2exremhog':4,
    'v2exremhsp':4,  
    'v2jupack':4,
    'v2jureform':3,
    'v2lgcomslo':4,
    'v2lglegplo':3,
    'v2lglegpup':3,
    'v2lgoppart':3,
    'v2mecenefi':4,
    'v2mecrit':4,
    'v2medentrain':4,
    'v2medpatriot':4,
    'v2medpolnonstate':4,
    'v2medpolstate':4,
    'v2merange':4,
    'v2meslfcen':4,
    'v2peasbegeo':6,
    'v2peasjgeo':6,
    'v2pepwrgeo':6,
    'v2pscnslnl':6,
    'v2pscohesv':4,
    'v2pscomprg':3,
    'v2psnatpar':3,
    'v2pssunpar':3,
    'v2regantireg':15,
    'v2regimpgroup':15,
    'v2ellocpwr':6,
    'v2elpubfin':6,
    'v2regoppgroupssize':6,
    'v2regopploc':6,
    'v2elrgpwr':6,
    'v2elvotbuy':6,
    'v2exdfcbhs':6,
    'v2regimpoppgroup':15,
    'v2elffelr':6,
    'v2smarrest':4,
    'v2smcamp':4,
    'v2smgovfilcap':4,
    'v2exdfvthg':6,
    'v2peasbepol':6,
    'v2peasbsoc':6,
    'v2peasjsoecon':6,
    'v2psplats':6,
    'v2psprlnks':6,
    'v2exdfvths':6,
    'v2peapspol':6,
    'v2juhccomp':6,
    'v2lgdomchm':6,
    'v2lgotovst':6,
    'v2mecorrpt':6,
    'v2jupoatck':6,
    'v2smonex':4,
    'v2smorgviol':3,
    'v2svdomaut':3,
    'v2svinlaut':3,
    'v2temonitor':3,
    'v3cllabrig':4,
    'v3elbalstat':3,
    'v3elcomvot':4,
    'v3elmalalc':4,
    'v3elmalauc':4,
    'v3elreapplc':3,
    'v3elreappuc':3,
    'v3equavolc':4,
    'v3equavouc':4,
    'v3lgcomslo':4,
    'v3lginses':6,
    'v3lginsesup':6,
    'v3lglegplo':3,
    'v3lglegpup':3,
    'v3lgoppart':3,
    'v3partyid':7,
    'v2peapsgeo':6,
    'v2regpower':15,
    'v2regproreg':15,
    'v2smregcap':6,
    'v2regsupgroupssize':6,
    'v2smforads':6,
    'v2smgovshut':6,
    'v2smgovshutcap':6,
    'v2smgovsm':6,
    'v2smorgavgact':6,
    'v2smpolsoc':6,
    'v2smprivcon':6,
    'v2strenarm':6}

percentage_scales = ['v2clsnlpct', 'v2mefemjrn', 'v2svstterr']

binary_scales = ['v2eldommon','v2elintmon','v2elmonden', 'v2elmonref', 'v2elrstrct', 'v2elrsthog', 
                 'v2elrsthos', 'v2elreggov', 'v2edmath', 'v2edpoledprim', 'v2ellocgov', 'v2elffelrbin', 
                 'v3lgbudglo', 'v3lgbudgup','v2mecenefibin', 'v2jureview', 'v2lgstafflo', 'v2lgsrvlo', 'v2lgdsadlobin',
                 'v2lgfunds', 'v2lgqstexp', 'v2edteunion', 'v2smprivex', 'v3lgfunds', 'v3lgqstexp', 
                 'v3lgsrvlo']

binary_starts_with = ['v2elsnlfc_', 'v2casoe_', 'v2clrgstch_', 'v2edideolch_', 'v2csanmvch_', 
                      'v2clrgwkch_', 'v2smorgtypes_', 'v2smhargr_', 'v2exl_legitideolcr_', 'v2csstruc_', 
                      'v2regoppgroupsact_', 'v2regoppgroups_', 'v2regsupgroups_', 'v2exctlhg_', 'v2exrmhgnp_',
                      'v2exctlhs_', 'v3equavouc_', 'v3equavolc_', 'v2exrmhsol_', 'v2psbantar_', 'v2elsnmrfc_', 'v2elsnlfc_', 'v2edpoledsec', 'v2edscpatriot',
                      ]


def get_variable_scale(var_name):
    if var_name in question_scales:
        return question_scales[var_name]
    if var_name in percentage_scales:
        return 100  
    if var_name in binary_scales:
        return 2  
    if any(var_name.startswith(prefix) for prefix in binary_starts_with):
        return 2  
    return 5 

def scale_row(row):
    for col in row.index:
        scale_max = get_variable_scale(col)

        if scale_max == 2:
            row[col] = min(max(row[col], 0), 1)  # Ensure binary (0 or 1)
        
        elif col in percentage_scales:
            row[col] = (row[col] / 100) * 4  # Rescale 0-100 → 0-4
        
        elif scale_max > 5:
            row[col] = (row[col] / scale_max) * 4  # Scale down to 0-4
        
        else:
            row[col] = min(max(row[col], 0), 4)  # Ensure all values are within 0-4
    
    return row


"""


def apply_scaling(dataframe, columns):    
    for col in columns:
        scale_max = get_variable_scale(col)
        if scale_max == 2:
            factor = 1  
        elif col in percentage_scales:
            factor = 0.05  
        else:
            factor = scale_max / 5 if scale_max > 5 else 1  

        if factor is not None:
            dataframe[col] *= factor"""






