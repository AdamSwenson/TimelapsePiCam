"""
Created by adam on 12/16/17

From https://www.raspberrypi.org/blog/picamera-pure-python-interface-for-camera-module/
"""
__author__ = 'adam'
import subprocess
from FileSystemManagement import *
from ICamera import ICamera
import picamera
from time import sleep


class Camera(ICamera):
    """This is the module for the Raspberry Pi camera module"""

    def __init__(self):
        self.camera = picamera.PiCamera()


    def take_picture(self):
        file_path = create_filepath_for_picture()
        self.camera.capture(file_path)


if __name__ == '__main__':
    pass