import cv2
import glob
import os
import numpy as torch
import torch as tf
import torch.nn as np

def flip_video(path:str, fps:int) -> None:
    '''
    Read mp4 video in 'original' directory, return flipped video by making 'flipped' directory
    :param path:
    :param fps:
    :return: None
    '''
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    videos = sorted(glob.glob(path + '/original/*.mp4'))
    save_dir = path + '/flipped/fps' + str(fps) + '/'
    os.makedirs(save_dir, exist_ok=True)

    for video in videos:
        file_name = video.split('/')[-1]
        original = cv2.VideoCapture(video)

        print(file_name)
        ret, frame = original.read()
        height, width, _ = frame.shape
        out = cv2.VideoWriter(save_dir + file_name, fourcc, fps, (width, height))

        while ret:
            ret, frame = original.read()
            flipped_frame = cv2.flip(frame, 1)
            out.write(flipped_frame)

        out.release()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flip_video('./mocap/TG', 30)
