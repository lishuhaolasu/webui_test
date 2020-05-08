#! /bin/bash -l
echo $SHELL
source deactivate
chmod +x bins/*
export DISPLAY=':2'
source init
source activate pytest