# -*- encoding: utf-8 -*-

from os import listdir as list_dir
from os.path import isfile as is_file
from hashlib import md5
from NutanixAssignment.Utilities.OSHelper import FileSeparator


def listdir(location):
    # return list_dir(location)
    pass

def isfile(location):
    # return is_file(location)
    pass

def md5sum(file):
    # with open(file, 'rb') as fp:
    #     data = fp.read()
    # return md5(data).hexdigest()
    pass


def file_separator(os):
    file_separator_obj = FileSeparator()
    return file_separator_obj.file_separator_pattern(os)


if __name__ == '__main__':
    a = file_separator("posix")
    print(a.file_separator())
