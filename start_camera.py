"""
Created by adam on 12/2/17
"""
__author__ = 'adam'
import cv2

from FileSystemManagement import *


def take_picture():
    camera_port = 0
    camera = cv2.VideoCapture(camera_port)
    time.sleep(0.1)  # If you don't wait, the image will be dark
    return_value, image = camera.read()
    file_path = create_filepath_for_picture()
    cv2.imwrite(file_path, image)
    del (camera)  # so that others can use the camera as soon as possible


def run():
    limit = 100
    count = 0

    while count < limit:
        take_picture()
        print("picture taken")
        time.sleep(PIC_DELAY)
        count += 1


if __name__ == '__main__':
    run()
