from sklearn import datasets, svm, metrics

import argparse
import cv2
import h5py
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pdb
import pickle

path_prefix = '../../Whale_ID/'

# read data
# data_file = path_prefix + 'train.csv'
# data = pd.read_csv(data_file)
# with open('train_data.pickle', 'wb') as f:
#     pickle.dump(data, f)

with open('train_data.pickle', 'rb') as f:
    data = pickle.load(f)
whale_image_names = data['Image']
whale_id = data['Id']
n_samples = len(whale_id)
whale_images = []


with h5py.File('whale_data.hdf5', 'w') as f:
    grp_id = f.create_group('whale_id')
    grp_im_name = f.create_group('image_name')
    grp_im = f.create_group('whale_images')
    for i in range(n_samples):
        image_name = whale_image_names[i]
        image = cv2.imread(path_prefix + 'train/' + image_name)
        id = whale_id[i]
        # print('i={},\tID={}\n'.format(i, id))
        grp_id.create_dataset('{}'.format(i), data=id)
        grp_im_name.create_dataset('{}'.format(i), data=image_name)
        grp_im.create_dataset('{}'.format(i), data=image)
        # whale_images.append(image.reshape(1, -1)[0])


with h5py.File('whale_data.hdf5', 'r') as f:
    i = 0
    for key in f['whale_images'].keys():
        ww = f['whale_images'][key].value
        i += 1
        
# pdb.set_trace()
# f = h5py.File('whale_data.hdf5', 'r+')
# print(1)

# with open('whale_images.pickle', 'wb') as f:
#     pickle.dump(whale_images, f)
# print(2)
# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title('Whale: {}, ID: {}'.format(image_name, id))
# plt.show()


# data = whale_images.values.reshape((n_samples, -1))
#
# if __name__ == '__main__':
#
#     parser = argparse.ArgumentParser(
#         description=(
#             'Categorizes whales using their flukes using machine'
#             'learning'))
#     parser.add_argument(
#         'file',
#         nargs='?',
#         default='images/01164v.jpg',
#         help='specify the path to gps log, default=images/01164v.jpg')
#
#     args = parser.parse_args()
#     if len(sys.argv) == 1:
#         parser.print_help()
#         args.file = 'images/01164v.jpg'
#         print('\nno image specfied, using default image.. \n')
