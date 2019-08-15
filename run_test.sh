#!/bin/bash


# 1 read out folder

LOCAL_COMPUTE=false
DEBUG=false
CLUSTER='x-men'
TESTRUN=true

TESTDIR_FULL=$1
TESTDIR=$(basename $TESTDIR_FULL)

CODEDIR=$(pwd);

# use timestamp + TESTDIR as working dir name
WDIR=$(date +"%y%m%d_%H%M%S")"_"$TESTDIR;



# 2 copy to location with appropriate file name

mkdir -p ../testing/$WDIR

#rsync -a --exclude='*~' --exclude='.git' \
rsync -a --exclude='*~' --exclude='analysis/' \
      $CODEDIR/ ../testing/$WDIR/code/

rsync -a --delete --exclude='*~' --exclude='__pycache__' \
      $CODEDIR/../analysis-dev/ ../testing/$WDIR/code/analysis



cd ../testing/$WDIR



# 3 read out simulation set up (cores, memory etc...)

source "./code/"$TESTDIR_FULL"simulation.config"

# echo $NPARSIM
# echo $NCORES
# echo $MEMGB


# 4 replace explored_params

cp "./code/"$TESTDIR_FULL"explored_params.py" ./code/net/


# 5 start simulation through run_local with settings from 3)

rm -f nohup.out

nohup ./code/run_local.sh $WDIR $CODEDIR $NPARSIM \
                          $NCORES $MEMGB $LOCAL_COMPUTE \
                          $CLUSTER $TESTRUN &



# # 6 run python script to analyze expected outputs


# # 7 copy log file produced by python 


# # 8 (optional) self destruct





# mkdir -p ../running/$TIMESTAMP

# #rsync -a --exclude='*~' --exclude='.git' \
# rsync -a --exclude='*~' --exclude='analysis/' \
#       $CODEDIR/ ../running/$TIMESTAMP/code/

# rsync -a --delete --exclude='*~' --exclude='__pycache__' \
#       $CODEDIR/../analysis-dev/ ../running/$TIMESTAMP/code/analysis

# cd ../running/$TIMESTAMP

# # make sure nohup.out doesn't exist
# touch nohup.out
# rm nohup.out

# if [[ ! -z $DESCRIPTION ]]
# then
#    echo $DESCRIPTION > ./description
# fi

# if $DEBUG
# then
#    echo "debug mode" 
#    ./code/run_local.sh $TIMESTAMP $CODEDIR $NPARSIM \
#                           $NCORES $MEMGB $LOCAL_COMPUTE \
#                           $CLUSTER $TESTRUN 
# else
#     echo "normal mode"
#     nohup ./code/run_local.sh $TIMESTAMP $CODEDIR $NPARSIM \
#                           $NCORES $MEMGB $LOCAL_COMPUTE \
#                           $CLUSTER $TESTRUN &
# fi

# # # touch $CODEDIR/../$TIMESTAMP


# # # run via sbatch -p x-men -c <ncores> --mem 32GB run.sh <ncores>

# # # echo "START"
# # # running -p x-men -c $1 --mem 32GB python stdp_scl_it_strct_run.py -c $1
# # # echo "END"
# # # touch end.org
