from sklearn import svm, metrics
from data_io import load_cropped_train_data, load_cropped_test_data

import argparse
import cv2
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import pickle
import pdb


# plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
# plt.title('Whale: {}, ID: {}'.format(image_name, id))
# plt.show()

def train_classifier(ids, image_names, images):
    n_samples = len(ids)

    print('Running the classifier...')
    resize_h = 100
    resize_w = 120

    whales = np.zeros((n_samples, resize_h * resize_w))
    i = 0
    for image in images:
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray, (resize_h, resize_w))
        whales[i, :] = resized_image.reshape(1, -1)[0].astype(np.float64)
        i += 1
    psb.set_trace()
    classifier = svm.SVC(verbose=True)#, probability=True)
    classifier.fit(whales, ids)

    # print('Predicting ...')
    # expected = ids[n_samples // 200:]
    # predicted = classifier.predict(whales[n_samples // 200:])
    #
    # print('Classification report for classifier {}:\n{}\n'.format(
    #       classifier,  metrics.classification_report(expected, predicted)
    #       ))
    # print('Confusion matrix:\n{}'.format(metrics.confusion_matrix(expected,
    #       predicted)))

    return classifier, whales


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
    parser.add_argument(
        '-t', '--train_data',
        default=False, action='store_true',
        help=('Train the classifier')
    )

    args = parser.parse_args()
    path_prefix = args.path
    read_data_again = args.read_data_again
    read_all_data = args.read_all_data
    train_data = args.train_data

    skip_new_whales = True

    ids, image_names, images = load_cropped_train_data(path_prefix,
        read_data_again, read_all_data, skip_new_whales)

    pdb.set_trace()
    if train_data:
        clf, whales = train_classifier(ids, image_names, images)
        with open('trained_classifier_cropped.pkl', 'wb') as f:
            pickle.dump(clf, f)
    else:
        with open('trained_classifier_cropped.pkl', 'rb') as f:
            clf = pickle.load(f)

    test_image_names, test_images = load_cropped_test_data(path_prefix,
        read_data_again, read_all_data)
    print('Predicting ...')
    n_samples= len(test_images)
    resize_h = 100
    resize_w = 120
    test_whales = np.zeros((n_samples, resize_h * resize_w))
    i = 0
    for image in test_images:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray, (resize_h, resize_w))
        test_whales[i, :] = resized_image.reshape(1, -1)[0].astype(np.float64)
        i += 1

    i = 0
    train_whales = np.zeros((len(ids), resize_h * resize_w))
    for image in images:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        resized_image = cv2.resize(gray, (resize_h, resize_w))
        train_whales[i, :] = resized_image.reshape(1, -1)[0].astype(np.float64)
        i += 1

    expected = ids[0:1]
    predicted = clf.predict(train_whales[:1])

    print('Classification report for classifier {}:\n{}\n'.format(
          clf,  metrics.classification_report(expected, predicted)
          ))
    print('Confusion matrix:\n{}'.format(metrics.confusion_matrix(expected,
          predicted)))

    predicted = clf.predict(test_whales)
    with open('predicted_test_whales_cropped.pkl', 'wb') as f:
        pickle.dump(predicted, f)
        pickle.dump(test_image_names, f)

    all_test_files_path = os.path.join('..', '..', 'Whale_ID', 'test')
    all_test_data = []
    all_count = 0
    for im in os.listdir(all_test_files_path):
        if im.endswith('.jpg'):
            all_count += 1
            all_test_data.append(im)
    print('All images in test dir: {}'.format(all_count))
    print('Predicted images: {}'.format(len(predicted)))
    print('Categorizing unidentified whales as new_whales ...')
    added_count = 0
    predicted_list = predicted.tolist()
    for whale in all_test_data:
        if not whale in test_image_names:
            added_count += 1
            # pdb.set_trace()
            predicted_list.append('new_whale')
            test_image_names.append(whale)
    print('Added {} new_whales'.format(added_count))
    # pdb.set_trace()

    out_data = {'Image':test_image_names, 'Id':predicted_list}
    df = pd.DataFrame(data=out_data)
    df.to_csv('predictions.csv', index=False, columns=['Image', 'Id'])
    pdb.set_trace()
