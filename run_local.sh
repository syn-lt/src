#!/bin/sh

echo ""
echo ""
echo "Running " $1
echo ""

if $8
then
    TESTFLAG='-t'
    DESTINATION='tests'
else
    TESTFLAG=''
    DESTINATION='completed'
fi


if $6
then
   echo "doing local"
   python -m code.net.xstrct_run -c $3 $TESTFLAG
else
   echo "doing nonlocal"
   srun -p $7 -c $4 --mem $5 --time 29-00 python -m code.net.xstrct_run -c $3 $TESTFLAG
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


CRDIR=$(pwd);


mkdir -p ../../$DESTINATION/
mv $CRDIR ../../$DESTINATION/$1

#echo "Not cleaning up, remove manually"
