#! /usr/bin/env bash

cd $PBS_O_WORKDIR
source /home/csdms/wmt/_testing/conda/bin/activate
python run_bmiilamb.py
