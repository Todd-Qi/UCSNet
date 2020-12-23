#!/usr/bin/env bash

save_path="./results/eth3d/"
test_list="./dataloader/datalist/eth3d/trainset.txt"
root_path="/mnt/B/qiyh/ETH3D/training/"

MAX_H=1280
MAX_W=1920

CUDA_VISIBLE_DEVICES=0 python test.py --root_path $root_path --test_list $test_list --save_path $save_path --max_h $MAX_H --max_w $MAX_W