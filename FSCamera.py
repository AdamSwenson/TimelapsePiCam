"""
Created by adam on 12/3/17
"""
__author__ = 'adam'
import subprocess
from FileSystemManagement import *
from ICamera import ICamera


class Camera(ICamera):

    def create_bash_command_string(self):
        file_path = create_filepath_for_picture()
        resolution = "-r 1280x720"
        other_options = "--no-banner"
        return "fswebcam %s %s %s" % (resolution, other_options, file_path)

    def take_picture(self):
        bashCommand = self.create_bash_command_string()
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()



if __name__ == '__main__':
    pass