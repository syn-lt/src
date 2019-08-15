from brian2.units import ms, mV, second, Hz
from pypet import cartesian_product

# test file

sigv = 1e-09/second

input_dict = {'T1': [1*second],
              'T2': [0.*second],
              'pp_tcut': [0.1*second],
              'T3': [0*second],
              'T4': [0*second],
              'syn_scl_rec' : [0],
              'syn_iscl_rec' : [0],
              'scl_rec_T' : [1*second],   
              'synEE_rec': [0],
              'synEI_rec': [0],
              'stdp_rec_T' : [25*second],
              'T5': [0*second],
              'crs_crrs_rec' : [0],
              'dt': [0.1*ms],
              'n_threads': [1],
              'N_e' : [400],
              'N_i' : [80],
              'tau_e': [5*ms],
              'tau_i': [10*ms],
              'NPInp': [1000],
              'NPInp_1n': [10],
              'NPInp_inh' : [1000],
              'NPInp_inh_1n': [10],
              'external_mode' : ['memnoise'],
              'mu_e' : [9.*mV],
              'mu_i' : [8.5*mV],
              'sigma_e': [0.5**0.5*mV],
              'sigma_i': [0.5**0.5*mV],
              'a_EPoi': [0.005],
              'PInp_rate': [1270*Hz],
              'PInp_inh_rate': [1250*Hz],
              'p_ee' : [0.15],
              'p_ei' : [0.5],
              'p_ie' : [0.15],
              'p_ii' : [0.5],
              'PInp_mode': ['pool'], # pool
              'syn_noise' : [0],
              'syn_sigma' : [sigv*1],
              'synEE_mod_dt' : [100*ms],
              'stdp_active': [1],
              'istdp_active': [1],
              'istdp_type' : ['sym'],
              'LTD_a' : [0.000005],
              'strct_active': [0],
              'strct_mode': ['zero'],
              'strct_c' : [0.002],
              'insert_P': [0.0002],
              'insert_P_ei': [0.00005],
              'istrct_active': [0],
              'p_inactivate': [0.01],
              'a_insert': [0.],
              'memtraces_rec' : [1],
              'getraces_rec' : [1],
              'gitraces_rec' : [1],
              'GExc_stat_dt' : [2*ms],
              'GInh_stat_dt' : [2*ms],
              'synee_atraces_rec' : [1],
              'synee_activetraces_rec' : [0],
              'synee_Apretraces_rec': [0],
              'synee_Aposttraces_rec': [0],
              'n_synee_traces_rec': [1000],
              'synEE_stat_dt' : [2*ms],
              'synei_atraces_rec' : [1],
              'synei_activetraces_rec' : [0],
              'synei_Apretraces_rec': [0],
              'synei_Aposttraces_rec': [0],
              'n_synei_traces_rec': [1000],
              'synEI_stat_dt' : [2*ms],              
              'synee_a_nrecpoints': [10],
              'synei_a_nrecpoints': [10],
              'synEEdynrec': [0],
              'synEIdynrec': [0],
              'syndynrec_dt': [1*second],
              'syndynrec_npts': [10],
              'turnover_rec': [0],
              'strct_dt' : [1000*ms],
              'spks_rec' : [1],
              'rates_rec': [1],
              'adjust_insertP': [0],
              'adjust_EI_insertP': [0],
              'csample_dt' : [10*second],
              'scl_active': [1],
              'iscl_active': [1],
              'dt_synEE_scaling': [25*ms],
              'eta_scaling': [0.25],
              'amax': [2.0],
              'Aplus': [0.0015],
              'Aminus': [-0.00075],
              'weight_mode': ['init'],
              'weight_path': ['weights/'],
              'a_ee' : [0.005],
              'a_ie' : [0.005],
              'a_ei' : [0.005],
              'a_ii' : [0.005],
              'ATotalMax': [0.2],#, 1.6/6, 1.8/6, 2.0/6],
              'iATotalMax': [0.7/6],#,1.0/6,1.2/6, 1.4/6, 1.6/6, 1.8/6],
              'ascale': [1.0],
              'Vt_e' : [-50.*mV],
              'Vt_i' : [-51*mV]}


name = 'test_poissonian_input'

explore_dict = cartesian_product(input_dict)

# explore_dict = {}

# n = max([len(item) for key,item in input_dict.items()])

# for key,item in input_dict.items():
#     if len(item) == n:
#         explore_dict[key] = item
#     elif len(item) == 1:
#         explore_dict[key] = item*n
#     else:
#         raise ValueError("items must be either n or 1")
