#!/bin/bash

rm -rf src/analysis
cp -r ~/lab/netw-mod/analysis-dev/ src/analysis/

python -m src.analysis.overview_winh
#python -m code.analysis.overview
#python -m src.analysis.t5_rasters
#python -m src.analysis.t5_peaks
