# -*- encoding: utf-8 -*-

from abc import ABC, abstractmethod
from NutanixAssignment.Utilities import Constant


class OSHelper(ABC):
    """
    Abstract Class OSHelper extends ABC and will have separate abstract methods defined which will be implemented in
    implementor classes. This will help us define Factory Pattern.
    """

    @abstractmethod
    def file_separator(self):
        """
        Abstract Method file_separator will be implemented by classes extending Abstract Class OSHelper
        :return:
        """
        pass


class WindowsOSHelper(OSHelper):

    def file_separator(self):
        """
        Implement abstract method file_separator from OSHelper.
        :return: String Character defining file separator used by Windows
        """
        return "\\"


class UnixOSHelper(OSHelper):

    def file_separator(self):
        """
        Implement abstract method file_separator from OSHelper.
        :return: String Character defining file separator used by Unix/Posix
        """
        return "/"


class FileSeparator:
    """
    FileSeparator is creator component of Factory Pattern. Depending upon type of OS specified, it will instantiate
    WindowsOSHelper or UnixOSHelper and return theie object which can be used to further call methods within those
    classes.
    """

    @staticmethod
    def file_separator_pattern(os):
        """
        file_separator_pattern will instantiate Windows or Unix Helper class based on parameter.
        :param os: String Param. Specifies on which os we want to check functionality
        :return: Object of Unix or Windows Helper class
        """
        if os in Constant.supported_platform:
            file_separator = {Constant.supported_platform[0]: WindowsOSHelper, Constant.supported_platform[1]: UnixOSHelper}
            return file_separator[os]()
        else:
            print(f"OS Platform is not supported")
            exit(1)


if __name__ == '__main__':
    a = FileSeparator.file_separator_pattern("windows")
    b = FileSeparator.file_separator_pattern("posix")
    # c = FileSeparator.file_separator_pattern('test')
    print(b.file_separator())
    print(a.file_separator())
    # print(c.file_separator())
