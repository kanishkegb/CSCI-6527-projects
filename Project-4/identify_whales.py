from sklearn import datasets, svm, metrics
from data_io import load_data

import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pdb


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
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description=(
            'Categorizes whales from their flukes using machine'
            'learning'))
    parser.add_argument(
        '-p', '--path',
        default='../../Whale_ID/',
        help='specify the path to the data downloaded from Kaggle'
    )
    parser.add_argument(
        '-r', '--read_data_again',
        default=False, action='store_true',
        help=('Read data again from the downloaded data. By default '
              'this reads from the saved hdf5 file')
    )
    parser.add_argument(
        '-a', '--read_all_data',
        default=False, action='store_true',
        help=('Read all data from the downloaded data. By default '
              'this reads only first 100')
    )

    args = parser.parse_args()
    path_prefix = args.path
    read_data_again = args.read_data_again
    read_all_data = args.read_all_data

    id, image_names, images = load_data(path_prefix, read_data_again,
                                        read_all_data)
    # pdb.set_trace()
