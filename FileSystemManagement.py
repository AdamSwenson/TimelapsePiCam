"""
Created by adam on 12/2/17
"""
__author__ = 'adam'

import os
import datetime
from config import *


def getSystemRoot():
    return os.getenv("HOME")


def make_timestamp_for_picture():
    """Creates the timestamp that will be used in the file name"""
    return datetime.datetime.now().strftime("%Y-%m-%d_%H%M")


def create_filepath_for_picture():
    """Creates the file path for a recently taken picture"""
    timeStamp = make_timestamp_for_picture()
    return "%s/%s/%s-%s.%s" % (getSystemRoot(), DATA_FOLDER_NAME, PIC_FILE_BASE, timeStamp, PIC_FILE_EXTN);




if __name__ == '__main__':
    pass