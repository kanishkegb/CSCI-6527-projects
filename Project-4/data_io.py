import cv2
import h5py
import pandas as pd
import pdb

def load_data(path_prefix, read_data_again, read_all_data):
    '''
    Loads data from the files provided from Kaggle

    Args:
        path_prefix: string - path to the data from Kaggle
        read_data_again: bool - whether to read data from the file again
        read_all_data: bool -  whether to read data all data
    Returns:
        whale_id: list - IDs for each whale image
        whale_image_names: list - name of the image
        whale_images: list - list of NxMx3 arrays for each whale image
    '''

    data_file = path_prefix + 'train.csv'
    data = pd.read_csv(data_file)
    whale_image_names = data['Image']
    whale_id = data['Id']
    n_samples = len(whale_id)

    if read_data_again:
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

    whale_images = []
    whale_image_names = []
    whale_id = []
    max_data = 10

    with h5py.File('whale_data.hdf5', 'r') as f:
        i = 0
        for key in f['whale_images'].keys():
            whale_images.append(f['whale_images'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['image_name'].keys():
            whale_image_names.append(f['image_name'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

        i = 0
        for key in f['whale_id'].keys():
            whale_id.append(f['whale_id'][key].value)
            i += 1
            if not read_all_data and i > max_data:
                break

    return whale_id, whale_image_names, whale_images


if __name__ == '__main__':
    path_prefix = '../../Whale_ID/'
    read_data_again = False
    read_all_data = False
    id, image_names, images = load_data(path_prefix, read_data_again,
                                        read_all_data)
    pdb.set_trace()
