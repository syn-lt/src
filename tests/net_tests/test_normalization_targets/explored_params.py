from brian2.units import ms, mV, second, Hz
from pypet import cartesian_product


input_dict = {'run_id' : [0,1,2,3],
              'ATotalMax': [0.2],
              'iATotalMax': [0.7/6],
              'sig_ATotalMax': [0., 0., 0.05, 0.],
              'sig_iATotalMax': [0., 0., 0., 0.025],
              'crs_crrs_rec': [0],
              'syn_scl_rec' : [0],
              'syn_iscl_rec' : [0],
              'synEE_rec': [0],
              'synEI_rec': [0],
              'syn_noise': [0]}


name = 'test_standard_net'

# explore_dict = cartesian_product(input_dict)

explore_dict = {}

n = max([len(item) for key,item in input_dict.items()])

for key,item in input_dict.items():
    if len(item) == n:
        explore_dict[key] = item
    elif len(item) == 1:
        explore_dict[key] = item*n
    else:
        raise ValueError("items must be either n or 1")


