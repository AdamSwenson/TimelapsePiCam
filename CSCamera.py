"""
Created by adam on 12/3/17
"""
__author__ = 'adam'
from FileSystemManagement import *
from ICamera import ICamera
import cv2
import time


class Camera(ICamera):

    def take_picture(self):
        camera = cv2.VideoCapture(CAMERA_PORT)
        time.sleep(0.1)  # If you don't wait, the image will be dark
        return_value, image = camera.read()
        file_path = create_filepath_for_picture()
        cv2.imwrite(file_path, image)
        print(" picture saved to %s" % file_path)
        del camera  # so that others can use the camera as soon as possible


if __name__ == '__main__':
    pass