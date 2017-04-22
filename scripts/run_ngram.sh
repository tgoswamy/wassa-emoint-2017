#!/usr/bin/env bash

CODEDIR=$(dirname "$0")"/../"

INPUT_FILE_PATH="/home/v2john/MEGA/Academic/Masters/UWaterloo/Research/WASSA-Task/dataset/anger-ratings-0to1.train.txt"

/usr/bin/python3 "$CODEDIR"/ngram_bootstrapper.py \
--input_file_path "$INPUT_FILE_PATH"
