import glob
import os
from natsort import natsorted

def rename_files(path:str) -> None:
    '''
    Remain only first numbers with file names split by _
    If it's two digits, change to three digits
    ex) 001_test.fbx -> 001.fbx
    ex) 12_test.fbx -> 012.fbx
    :param path:
    :return:None
    '''
    for file_name in natsorted(os.listdir(path)):
        new_name = file_name.split('_')[0] + '.' + file_name.split('.')[-1]
        if len(new_name.split('.')[0]) < 3:
            new_name = '0' + new_name
        os.rename(path + '/' + file_name, path + '/' + new_name)


if __name__ == '__main__':
    rename_files('./mocap_data/CILAB_EH')