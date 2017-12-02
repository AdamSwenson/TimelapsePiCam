"""
Created by adam on 12/2/17
"""
__author__ = 'adam'
import numpy as np
import cv2
from datetime import datetime, date, time

# Base Classes stuff
from FileSystemTools import *
from UtilityDecorators import *
from UtilityFunctions import *

DATA_FOLDER = "%s/Desktop/usb-camera-pics/" % getSystemRoot()

# These are used to create the file names of the pictures
PIC_FILE_BASE = "porsche-cam"
PIC_FILE_EXTN = "png"

PIC_DELAY = 60



if __name__ == '__main__':
    pass
