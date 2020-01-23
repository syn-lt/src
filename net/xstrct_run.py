import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as pl

import os, git, random

from pypet import Environment, Trajectory
import pypet.pypetexceptions as pex
from pypet.brian2.network import NetworkManager
from pypet.brian2.parameter import Brian2Parameter, \
                                   Brian2MonitorResult

from .explored_params import explore_dict, name

from .add_parameters import add_params
from .xstrct_netw import run_net
from .post_processing import post_process


# control the number of cores to be used for computation
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--ncores", "-c", help="No. cores", nargs=1)
parser.add_argument("--testrun", "-t", action='store_true')
parser.add_argument("--postprocess", "-x", action='store_true')
args = parser.parse_args()
ncores = int(args.ncores[0])

print("Using {:d} cores".format(ncores))


# check the state of the git repository
repo = git.Repo('./src/')

if not args.testrun:
    # check for changes, while ignoring submodules
    if repo.git.status('-s', '--ignore-submodules', '--untracked-files=no'):
        raise pex.GitDiffError('Found not committed changes!')

    commit = repo.commit(None)



filename = os.path.join(os.getcwd(), 'data/', name+'.hdf5')

# if not the first run, tr2 will be merged later
label = 'tr1'

# if only post processing, can't use the same label
# (generates HDF5 error)
if args.postprocess:
    label += '_postprocess-%.6d' % random.randint(0, 999999)

env = Environment(trajectory=label,
                  add_time=False,
                  filename=filename,
                  continuable=False, # ??
                  lazy_debug=False,  # ??
                  multiproc=True,     
                  ncores=ncores,
                  use_pool=False, # likely not working w/ brian2
                  wrap_mode='QUEUE', # ??
                  overwrite_file=False)


tr = env.trajectory

add_params(tr)

if not args.testrun:
    tr.f_add_parameter('mconfig.git.sha1', str(commit))
    tr.f_add_parameter('mconfig.git.message', commit.message)

tr.f_explore(explore_dict)


def run_sim(tr):
    try:
        run_net(tr)
    except TimeoutError:
        print("Unable to plot, must run analysis manually")

    post_process(tr)


if args.postprocess:
    env.run(post_process)
else:
    env.run(run_sim)



                  


