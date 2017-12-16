"""
Created by adam on 12/2/17

camera logic based on : https://www.raspberrypi.org/documentation/usage/webcams/
"""
__author__ = 'adam'

import time
from FileSystemManagement import *
from FSCamera import Camera

#
# class FSCamera:
#
#     def create_bash_command_string(self):
#         file_path = create_filepath_for_picture()
#         resolution = "-r 1280x720"
#         other_options = "--no-banner"
#         return "fswebcam %s %s %s" % (resolution, other_options, file_path)
#
#     def take_picture(self):
#         bashCommand = self.create_bash_command_string()
#         process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
#         output, error = process.communicate()
#
#
# class CV2Camera:
#
#     def take_picture(self):
#         import cv2
#         camera = cv2.VideoCapture(CAMERA_PORT)
#         time.sleep(0.1)  # If you don't wait, the image will be dark
#         return_value, image = camera.read()
#         file_path = create_filepath_for_picture()
#         cv2.imwrite(file_path, image)
#         print(" picture saved to %s" % file_path)
#         del camera  # so that others can use the camera as soon as possible
#


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

    #
    # while count < limit:
    #     camera.take_picture()
    #
    #     time.sleep(PIC_DELAY)
    #     count += 1
    #     print("picture #%s taken " % count)


if __name__ == '__main__':
    camera = Camera()
    timed_run_handler(camera)
