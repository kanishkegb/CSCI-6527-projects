from sklearn import datasets, svm, metrics

import matplotlib.pyplot as plt
import pandas as pd
import pickle

# read data
# data_file = '../../Whale_ID/train.csv'
# data = pd.read_csv(data_file)
# with open('train_data.pickle', 'r') as f:
#     pickle.dump(data, f)
with open('train_data.pickle', 'rb') as f:
    data = pickle.load(f)

# import pdb; pdb.set_trace()
# 
