from re import split
from recbole.quick_start import run_recbole

parameter_dict = {
    'model' : 'CDAE',  # model selection

    'data_path' : '../../data/',
    'dataset' : 'ls',   # data setting

    'USER_ID_FIELD' : 'pubchemID',
    'ITEM_ID_FIELD' : 'MeSH',
    'RATING_FIELD' : 'Score',

    'load_col' : {
        'inter': ['pubchemID', 'MeSH', 'Score']
    },

    'user_inter_num_interval': [0, 166], # interation num filter

    'eval_args' : {
        'group_by': 'user',
        'order': 'RO',
        'split': {'RS': [8, 1, 1]},
        'mode': 'uni100'
    },

    'metrics': ['RMSE', 'MAE', 'AUC', 'LogLoss'],
    'valid_metric': 'RMSE'
}

run_recbole(config_dict = parameter_dict)