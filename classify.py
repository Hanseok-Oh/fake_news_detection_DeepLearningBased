'''
for test new data
input: model, data, weight_matrix
output: accuracy, loss, plot
'''
from model.trainer import Trainer
from dataLoader import split_data
from model.bi_lstm import BiLSTM


import argparse
import torch
import numpy as np

def define_argparser():
    # argparse
    parser = argparse.ArgumentParser(description = 'run argparser')
    parser.add_argument('--model',required=False,default='bi-lstm', help='select model')
    parser.add_argument('--data_path',required=False,default = '', help='fake news data path (csv format), must include text, type columns')
    parser.add_argument('--weights_matrix',required=False,default = 'object/BiLSTM/weights_matrix_840B_300.npy', help='weights matrix path for word embeddings')
    args = parser.parse_args()
    return args

def main(args):
    # gpu 하나일 때 / colab 기준 환경
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    weights_matrix = np.load(args.weights_matrix, allow_pickle=True) # 새로 저장

    if args.model =='bi-lstm':
        model = BiLSTM(weights_matrix).to(device)
        model_path = ''

    elif args.model =='cnn':
        pass

    checkpoint = torch.load(model_path)
    state_dict = checkpoint['net']
    model.load_state_dict(state_dict=state_dict)

    cls = Trainer(args)
    cls.test(model, device)

if __name__ =='__main__':
    args =define_argparser()
    main(args)

