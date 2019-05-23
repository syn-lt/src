#!/bin/sh

#cd code/

echo "Running " $1

# make sure sbatch.out doesn't exist
touch sbatch.out
rm sbatch.out

srun -p x-men -c $4 --mem $5 --time 29-00 python -m code.xstrct_run -c $3
#python -m code.xstrct_run -c $3


#srun -p x-men -c $4 --mem $5 python hello_world.py --c $3

echo "Simulation finished."



# # with multiprocessing. currently defunct because of a problem
# # with tex locking and memory consumption issues
# srun -p x-men -c $4 --mem $5 python default_analysis.py data/*.hdf5 $3

# final zero sys.argv sets mode to sequential
#cd ../
#echo "Running analysis..."
#mv code/run_analysis_fb.sh .
#./run_analysis_fb.sh 


#rm -rf builds/
# echo "Copying data..."
# cp data/* $2/../data/

# echo "Copying nohup.out..."
# cp nohup.out $2/../data/$1.out

echo "Done."

CRDIR=$(pwd);
mv $CRDIR ../../completed/$1

#echo "Not cleaning up, remove manually"
