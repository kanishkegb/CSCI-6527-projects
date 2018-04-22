from sklearn import datasets, svm, metrics

import cv2
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import pandas as pd
import pickle

path_prefix = '../../Whale_ID/'

# read data
# data_file = path_prefix + 'train.csv'
# data = pd.read_csv(data_file)
# with open('train_data.pickle', 'r') as f:
#     pickle.dump(data, f)
with open('train_data.pickle', 'rb') as f:
    data = pickle.load(f)
whale_images = data['Image']
whale_id = data['Id']

for i in range(10):
    image_name = whale_images[i]
    image = cv2.imread(path_prefix + 'train/' + image_name)
    id = whale_id[i]
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Whale: {}, ID: {}'.format(image_name, id))
    plt.show()
import pdb; pdb.set_trace()
