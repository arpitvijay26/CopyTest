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

def removing_unwanted_chars_in_folder_location(source):
    """

    :param source:
    :return:
    """
    # if source.startswith('\'') and source.endswith('\''):
    #     source = source.replace('\'', '')
    if source[-1] == '/' or source[-1] == '\\':
        source = source[:-1]
    return source

if __name__ == '__main__':
    a = file_separator("posix")
    print(a.file_separator())
    print(removing_unwanted_chars_in_folder_location('/Users/arpit/'))
