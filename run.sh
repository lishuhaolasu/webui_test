#! /bin/bash
echo $SHELL
chmod +x bins/*
export DISPLAY=':2'
/home/lasu/miniforge3/condabin/conda init
/home/lasu/miniforge3/condabin/conda activate pytest