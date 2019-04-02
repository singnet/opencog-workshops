#!/bin/bash

source /home/relex/.profile
source /home/relex/miniconda3/bin/activate demo

# Start RelEx server
/home/relex/relex-master/target/appassembler/bin/relexd &

cd /home/relex/opencog-workshops-master/ && exec jupyter notebook --ip=0.0.0.0
