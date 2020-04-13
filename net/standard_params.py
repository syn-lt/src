
from brian2.units import *

N_e = 400
N_i = int(0.2*N_e)

tau = 20.*ms                 # membrane time constant

syn_cond_mode = 'exp'
syn_cond_mode_EI = 'exp'
tau_e = 5.*ms                # EPSP time constant
tau_i = 10.*ms               # IPSP time constant
tau_e_rise = 0.5*ms
tau_i_rise = 0.15*ms
norm_f_EE = 1.0
norm_f_EI = 1.0
El = -60.*mV                 # resting value
Ee = 0.*mV                   # reversal potential Excitation 
Ei = -80.*mV                 # reversal potential Inhibition
mu_e = 9.0*mV
mu_i = 8.5*mV
sigma_e = 0.5**0.5*mV        # noise amplitude
sigma_i = 0.5**0.5*mV

Vr_e = -60.*mV
Vr_i = -60.*mV
Vt_e = -50.*mV
Vt_i = -51.*mV

ascale = 1.0
a_ee = 0.005
a_ie = 0.005
a_ei = 0.005
a_ii = 0.005

p_ee = 0.15
p_ie = 0.15
p_ei = 0.5
p_ii = 0.5

taupre = 15*ms
taupost = 30*ms
Aplus = 0.0015
Aminus = -0.00075
amax = 2.0


external_mode = 'memnoise'

# poisson 
PInp_mode = 'pool' #indep
NPInp = 1000
NPInp_1n = 10
NPInp_inh = 1000
NPInp_inh_1n = 10
PInp_rate = 1270*Hz
PInp_inh_rate = 1250*Hz
a_EPoi = 0.005
a_IPoi = 0.
p_EPoi = 0.2
p_IPoi = 0.1

# synapse noise
syn_noise = 1
syn_noise_type = 'additive'
syn_sigma = 1e-09/second
synEE_mod_dt = 100*ms

#STDP
stdp_active = 1
synEE_rec = 1
ATotalMax = 0.2
sig_ATotalMax = 0.05

#iSTDP
istdp_active = 1
istdp_type = 'sym' #'dbexp'
taupre_EI = 20*ms
taupost_EI = 20*ms
synEI_rec = 1
LTD_a = 0.000005

# scaling
scl_active = 1
dt_synEE_scaling = 25*ms
eta_scaling = 0.25

# iscaling
iscl_active = 1
iATotalMax = 0.7/6
sig_iATotalMax = 0.025
syn_iscl_rec = 0

# structural plasticity
strct_active = 1
strct_mode = 'zero'
prn_thrshld = 0.001 * ATotalMax
insert_P = 0.0002
strct_dt = 1000*ms
a_insert = 0.
p_inactivate = 0.01
strct_c = 0.002

# inhibitory structural plasticity
istrct_active = 0
insert_P_ei = 0.00005
p_inactivate_ei = 0.25


# intrinsic plasticity
it_active = 0
eta_ip = 0.2*mV*ms
it_dt = 10*ms
h_ip = 3*Hz


#preT  = 100*second
T1 = 1*second
T2 = 10*second
T3 = 1*second
T4 = 1*second
T5 = 5*second
dt = 0.1*ms
n_threads = 1

# neuron_method = 'euler'
# synEE_method = 'euler'


# recording
memtraces_rec = 1
vttraces_rec = 1
getraces_rec = 1
gitraces_rec = 1
gfwdtraces_rec = 1
rates_rec = 1

nrec_GExc_stat = 3
nrec_GInh_stat = 3
GExc_stat_dt = 2.*ms
GInh_stat_dt = 2.*ms

synee_atraces_rec = 1
synee_activetraces_rec = 0
synee_Apretraces_rec = 1
synee_Aposttraces_rec = 1
n_synee_traces_rec = 1000
synEE_stat_dt = 2.*ms

synei_atraces_rec = 1
synei_activetraces_rec = 1
synei_Apretraces_rec = 1
synei_Aposttraces_rec = 1
n_synei_traces_rec = 1000
synEI_stat_dt = 2.*ms


syn_scl_rec = 1
stdp_rec_T = 1.*second
scl_rec_T = 0.1*second

synEEdynrec = 1
synEIdynrec = 1
syndynrec_dt = 1*second
syndynrec_npts = 10

turnover_rec = 1
spks_rec = 1
T2_spks_rec = 0
synee_a_nrecpoints = 10
synei_a_nrecpoints = 10

crs_crrs_rec = 1

adjust_insertP = 0
adjust_EI_insertP = 0
csample_dt = 10*second

# post processing
pp_tcut = 1*second

# weight modes
basepath = '/home/hoffmann/lab/netw_mods/z2/'
weight_mode = 'init'
weight_path = 'weights/'

run_id = 0 # doesn't do anything, added for running 
           # multiple copies for testing
random_seed = 578
