#!/usr/bin/env bash


save_path="/mnt/H/qiyh/UCSNet/results/dtu_results/"
test_list="./dataloader/datalist/dtu/test.txt"
root_path="/mnt/G2/dataset_qiyh/MVSNet/preprocessed_inputs/dtu/"


CUDA_VISIBLE_DEVICES=0 python test.py --root_path $root_path --test_list $test_list --save_path $save_path --max_h 1200 --max_w 1600
