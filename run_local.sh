#!/bin/sh

echo "Running " $1

cd code/

if $6
then
   python -m net.xstrct_run -c $3
else
   srun -p $7 -c $4 --mem $5 --time 29-00 python -m net.xstrct_run -c $3
fi

# # with multiprocessing. currently defunct because of a problem
# # with tex locking and memory consumption issues
# srun -p x-men -c $4 --mem $5 python default_analysis.py data/*.hdf5 $3

# final zero sys.argv sets mode to sequential
#cd ../
#echo "Running analysis..."
#mv code/run_analysis_fb.sh .
#./run_analysis_fb.sh 

echo "Done."
cd ../

CRDIR=$(pwd);

if $8
then
    DESTINATION='tests'
else
    DESTINATION='completed'
fi

mkdir -p ../../$DESTINATION/
mv $CRDIR ../../$DESTINATION/$1

#echo "Not cleaning up, remove manually"
