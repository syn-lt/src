#!/bin/sh

# first get the current working directory
CODEDIR=$(pwd);

# use timestamp as temporary folder name
TIMESTAMP=$(date +"%Y-%m-%d_%H-%M-%S");

mkdir ../running/$TIMESTAMP

#rsync -a --exclude='*~' --exclude='.git' \
rsync -a --exclude='*~' \
      $CODEDIR/ ../running/$TIMESTAMP/code/

rsync -a --exclude='.git' --exclude='*~' --exclude='__pycache__' \
      $CODEDIR/../analysis/ ../running/$TIMESTAMP/analysis

cd ../running/$TIMESTAMP

# make sure nohup.out doesn't exist
touch nohup.out
rm nohup.out

NPARSIM=$1;
NCORES=$2;
MEMGB=$3;

nohup ./code/run_local.sh $TIMESTAMP $CODEDIR $NPARSIM $NCORES $MEMGB &

# touch $CODEDIR/../$TIMESTAMP


# run via sbatch -p x-men -c <ncores> --mem 32GB run.sh <ncores>

# echo "START"
# running -p x-men -c $1 --mem 32GB python stdp_scl_it_strct_run.py -c $1
# echo "END"
# touch end.org
