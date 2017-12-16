"""
Created by adam on 12/2/17

camera logic based on : https://www.raspberrypi.org/documentation/usage/webcams/
"""
__author__ = 'adam'

import time
from FileSystemManagement import *
from PICamera import Camera


def timed_run_handler(camera, limit=100):
    count = 0

    while count < limit:
        camera.take_picture()
        time.sleep(PIC_DELAY)
        count += 1
        print("picture #%s taken " % count)


def run():
    limit = 100
    count = 0


if __name__ == '__main__':
    camera = Camera()
    timed_run_handler(camera)
