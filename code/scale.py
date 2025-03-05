# default is 5 unless otherwise specified (0-4 scale)
question_scales = {
    'v2caconmob': 4,    
    'v2clgeocl':6,
    'v2clprptym':6,
    'v2clprptyw':6,
    'v2clrgunev':3, 
    'v2cscnsult':2,
    'v2csprtcpt':3,
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
    'v2lgcomslo':3,
    'v2lglegplo':3,
    'v2lglegpup':3,
    'v2lgoppart':3,
    'v2mecenefi':3,
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
    'v2regantireg':14,
    'v2regimpgroup':14,
    'v2regimpoppgroup':14,
    'v2smarrest':4,
    'v2smcamp':4,
    'v2smgovfilcap':4,
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
    }

percentage_scales = ['v2clsnlpct', 'v2mefemjrn', 'v2svstterr']

binary_scales = ['v2eldommon','v2elintmon','v2elmonden', 'v2elmonref', 'v2elrstrct', 'v2elrsthog', 
                 'v2elrsthos', 'v2elreggov', 'v2edmath', 'v2edpoledprim', 'v2ellocgov', 'v2elffelrbin', 
                 'v3lgbudglo', 'v3lgbudgup','v2mecenefibin', 'v2jureview', 'v2lgstafflo', 'v2lgsrvlo', 'v2lgdsadlobin',
                 'v2lgfunds', 'v2lgqstexp', 'v2edteunion', 'v2smprivex', 'v2smregcap', 'v3lgfunds', 'v3lgqstexp', 
                 'v3lgsrvlo']

binary_starts_with = ['v2elsnlfc_', 'v2casoe_', 'v2clrgstch_', 'v2edideolch_', 'v2csanmvch_', 
                      'v2clrgwkch_', 'v2smorgtypes_', 'v2smhargr_', 'v2exl_legitideolcr_', 'v2csstruc_', 
                      'v2regoppgroupsact_', 'v2regoppgroups_', 'v2regsupgroups_', 'v2exctlhg_', 'v2exrmhgnp_',
                      'v2exctlhs_', 'v2exrmhsol_', 'v2psbantar_', 'v2elsnmrfc_', 'v2elsnlfc_', 'v2edpoledsec', 'v2edscpatriot',
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



