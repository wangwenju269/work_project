# -*- coding:utf-8 -*-
import os
cur_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
import argparse
parser = argparse.ArgumentParser(description="train")
parser.add_argument("--train_path", type=str, default= f'{cur_dir}/data/train.json',help="train file")
parser.add_argument("--dev_path", type=str, default=   f'{cur_dir}/data/dev.json',    help="test file")
parser.add_argument("--test_path", type=str, default=  f'{cur_dir}/data/test2.json', help="test file")
parser.add_argument("--checkpoints", type=str, default="./check_point/text_cluster.pth",help="output_dir")
parser.add_argument("--batch_size", type=int, default = 96 ,help="batch_size")
parser.add_argument("--max_length", type=int, default = 48, help="max_length")
parser.add_argument("--hidden", type=int, default = 512,help="the numbers of hidden state lays")
parser.add_argument("--num_dimension", type=int, default = 128,help="Dimensionality reduction")
parser.add_argument("--rel_num", type=int, default = 9,  help="K_means算法聚类总数")
parser.add_argument("--drop", type=float, default = 0.5,help="dropout")
parser.add_argument("--epoch", type=int, default=7,help="epoch")
parser.add_argument("--step", type=int, default=100,help="how much step to write log")
parser.add_argument("--learning_rate", type=float, default=2e-5,help="learning_rate")
parser.add_argument("--require_improvement", type=int, default=100,help="require_improvement")
parser.add_argument("--pretrained_model_path", type=str, default=f'{cur_dir}/pretrained_model/chinese_roberta_wwm_ext',help="pretrained_model_path")
parser.add_argument("--clip_norm", type=str, default=0.25,help="clip_norm")
parser.add_argument("--warm_up_epoch", type=str, default=1,help="warm_up_steps")
parser.add_argument("--decay_epoch", type=str, default=5,help="decay_steps")
parser.add_argument("--output", type=str, default=f'{cur_dir}/output/result.json',help="output")
args = parser.parse_args()
