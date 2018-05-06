from shutil import copyfile
import os
import pandas as pd


def copy_cropped_images(file_name):

    print('Starting copying files to train crop data ...')
    df = pd.read_csv(file_name)
    image_names = df['filename']

    directory = os.path.dirname(os.path.join('..', '..', '..', 'Whale_ID',
                                'crop_train'))
    if not os.path.exists(directory):
        os.makedirs(directory)

    for image_name in image_names:
        src = os.path.join(os.getcwd(), '..', '..', '..', 'Whale_ID', 'train',
                           image_name)
        dst =  os.path.join(os.getcwd(), '..', '..', '..', 'Whale_ID',
                            'crop_train', image_name)
        copyfile(src, dst)

    print('Finished copying.')


if __name__ == '__main__':

    import pdb

    file_name = 'annotations/whale_cropped.csv'
    copy_cropped_images(file_name)
