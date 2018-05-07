import cv2
import h5py
import matplotlib.pyplot as plt
import os
import pandas as pd
import pdb


def load_data(path_prefix, read_data_again, read_all_data, skip_new_whales):
    '''
    Loads training data from the files provided from Kaggle

    Args:
        path_prefix: string - path to the data from Kaggle
        read_data_again: bool - whether to read data from the file again
        read_all_data: bool -  whether to read data all data
        skip_new_whales: bool - whether to skip the 'new_whale' IDs
    Returns:
        whale_id: list - IDs for each whale image
        whale_image_names: list - name of the image
        whale_images: list - list of NxMx3 arrays for each whale image
    '''

    print('Loading data ...')
    data_file = path_prefix + 'train.csv'
    data = pd.read_csv(data_file)
    whale_image_names = data['Image']
    whale_id = data['Id']
    n_samples = len(whale_id)

    if read_data_again:
        print('Saving {} items into hdf5 ...'.format(n_samples))
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
        print('Saving data into hdf5 completed.')

    whale_images = []
    whale_image_names = []
    whale_id = []
    max_data = 100

    if read_all_data:
        print('Reading all data from hdf5 file ...')
    else:
        print('Reading first {} data from hdf5 file ...'.format(max_data))

    with h5py.File('whale_data.hdf5', 'r') as f:
        i = 0
        for key in f['whale_images'].keys():
            if skip_new_whales and f['whale_id'][key].value=='new_whale':
                continue
            whale_images.append(f['whale_images'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['image_name'].keys():
            if skip_new_whales and f['whale_id'][key].value=='new_whale':
                continue
            whale_image_names.append(f['image_name'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['whale_id'].keys():
            if skip_new_whales and f['whale_id'][key].value=='new_whale':
                continue
            whale_id.append(f['whale_id'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

    print('Reading data completed.')

    return whale_id, whale_image_names, whale_images


def load_test_data(path_prefix, read_data_again, read_all_data):
    '''
    Loads test data from the files provided from Kaggle

    Args:
        path_prefix: string - path to the data from Kaggle
        read_data_again: bool - whether to read data from the file again
        read_all_data: bool -  whether to read data all data
    Returns:
        whale_image_names: list - name of the image
        whale_images: list - list of NxMx3 arrays for each whale image
    '''

    if read_data_again:
        print('Saving data into hdf5 ...')
        with h5py.File('whale_test_data.hdf5', 'w') as f:
            grp_im_name = f.create_group('image_name')
            grp_im = f.create_group('test_images')
            i = 0
            for im in os.listdir('{}test/'.format(path_prefix)):
                if im.endswith('.jpg'):
                    image = cv2.imread('{}test/{}'.format(path_prefix, im))
                    grp_im.create_dataset('{}'.format(i), data=image)
                    grp_im_name.create_dataset('{}'.format(i), data=im)
                    i += 1

        print('Saving {} data into hdf5 completed.'.format(i))


    print('Loading test data ...')
    whale_images = []
    whale_image_names = []

    max_data = 100

    if read_all_data:
        print('Reading all test data from hdf5 file ...')
    else:
        print('Reading first {} test data from hdf5 file ...'.format(max_data))

    with h5py.File('whale_test_data.hdf5', 'r') as f:
        i = 0
        for key in f['test_images'].keys():
            whale_images.append(f['test_images'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['image_name'].keys():
            whale_image_names.append(f['image_name'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break


    print('Reading data completed.')

    return whale_image_names, whale_images

def load_cropped_train_data(path_prefix, read_data_again, read_all_data, skip_new_whales):
    '''
    Loads training data from the files provided from Kaggle

    Args:
        path_prefix: string - path to the data from Kaggle
        read_data_again: bool - whether to read data from the file again
        read_all_data: bool -  whether to read data all data
        skip_new_whales: bool - whether to skip the 'new_whale' IDs
    Returns:
        whale_id: list - IDs for each whale image
        whale_image_names: list - name of the image
        whale_images: list - list of NxMx3 arrays for each whale image
    '''

    print('Loading data ...')
    data_file = os.path.join('..', '..', 'Whale_ID', 'train.csv')
    data = pd.read_csv(data_file)
    whale_image_names = data['Image']
    whale_id = data['Id']
    n_samples = len(whale_id)

    if read_data_again:
        print('Checking cropped data ...')
        cropped_images = []
        for im in os.listdir('cropped_train_images'):
            if im.endswith('.jpg'):
                cropped_images.append(im)
        print('Cropped images: {}'.format(len(cropped_images)))

        print('Saving {} items into hdf5 ...'.format(n_samples))
        with h5py.File('cropped_train_data.hdf5', 'w') as f:
            grp_id = f.create_group('whale_id')
            grp_im_name = f.create_group('image_name')
            grp_im = f.create_group('whale_images')
            skip_count = 0
            for i in range(n_samples):
                image_name = whale_image_names[i]
                image_path = os.path.join('..', '..', 'Whale_ID', 'train', image_name)
                image = cv2.imread(image_path)
                id = whale_id[i]
                # print('i={},\tID={}\n'.format(i, id))

                if not image_name in cropped_images:
                    print('skipping {}'.format(image_name))
                    skip_count += 1
                    id = 'new_whale'

                grp_id.create_dataset('{}'.format(i), data=id)
                grp_im_name.create_dataset('{}'.format(i), data=image_name)
                grp_im.create_dataset('{}'.format(i), data=image)
                # whale_images.append(image.reshape(1, -1)[0])
            print('No whales detected in {} images'.format(skip_count))
        print('Saving data into hdf5 completed.')

    whale_images = []
    whale_image_names = []
    whale_id = []
    max_data = 100

    if read_all_data:
        print('Reading all data from hdf5 file ...')
    else:
        print('Reading first {} data from hdf5 file ...'.format(max_data))

    with h5py.File('cropped_train_data.hdf5', 'r') as f:
        i = 0
        for key in f['whale_images'].keys():
            if skip_new_whales and f['whale_id'][key].value=='new_whale':
                continue
            whale_images.append(f['whale_images'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['image_name'].keys():
            if skip_new_whales and f['whale_id'][key].value=='new_whale':
                continue
            whale_image_names.append(f['image_name'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['whale_id'].keys():
            if skip_new_whales and f['whale_id'][key].value=='new_whale':
                continue
            whale_id.append(f['whale_id'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

    print('Reading data completed.')

    return whale_id, whale_image_names, whale_images


def load_cropped_test_data(path_prefix, read_data_again, read_all_data):
    '''
    Loads test data from the files provided from Kaggle

    Args:
        path_prefix: string - path to the data from Kaggle
        read_data_again: bool - whether to read data from the file again
        read_all_data: bool -  whether to read data all data
    Returns:
        whale_image_names: list - name of the image
        whale_images: list - list of NxMx3 arrays for each whale image
    '''

    if read_data_again:
        print('Saving data into hdf5 ...')
        with h5py.File('cropped_test_data.hdf5', 'w') as f:
            grp_im_name = f.create_group('image_name')
            grp_im = f.create_group('test_images')
            i = 0
            for im in os.listdir('cropped_test_images'):
                if im.endswith('.jpg'):
                    image = cv2.imread(os.path.join('cropped_test_images', im))
                    grp_im.create_dataset('{}'.format(i), data=image)
                    grp_im_name.create_dataset('{}'.format(i), data=im)
                    i += 1

        print('Saving {} data into hdf5 completed.'.format(i))


    print('Loading test data ...')
    whale_images = []
    whale_image_names = []

    max_data = 100

    if read_all_data:
        print('Reading all test data from hdf5 file ...')
    else:
        print('Reading first {} test data from hdf5 file ...'.format(max_data))

    with h5py.File('cropped_test_data.hdf5', 'r') as f:
        i = 0
        for key in f['test_images'].keys():
            whale_images.append(f['test_images'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['image_name'].keys():
            whale_image_names.append(f['image_name'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break


    print('Reading data completed.')

    return whale_image_names, whale_images


if __name__ == '__main__':
    # path_prefix = '../../Whale_ID/'
    # read_data_again = False
    # read_all_data = False
    # id, image_names, images = load_data(path_prefix, read_data_again,
    #                                     read_all_data)
    # path_prefix = '../../Whale_ID/'
    # read_data_again = False
    # read_all_data = False
    # image_names, images = load_test_data(path_prefix, read_data_again,
    #                                      read_all_data)
    #
    path_prefix = ''
    read_data_again = True
    read_all_data = True
    skip_new_whales = False
    # whale_id, whale_image_names, whale_images = load_cropped_train_data(path_prefix,
    #     read_data_again, read_all_data, skip_new_whales)
    whale_image_names, whale_images = load_cropped_test_data(path_prefix,
        read_data_again, read_all_data)

    pdb.set_trace()
    # plt.imshow(cv2.cvtColor(images[0], cv2.COLOR_BGR2RGB))
    # plt.title('Whale: {}, ID: {}'.format(image_name, id))
    # plt.show()
