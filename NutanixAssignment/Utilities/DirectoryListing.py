# -*- encoding: utf-8 -*-

from NutanixAssignment.Utilities.CommonHelper import listdir, isfile, removing_unwanted_chars_in_folder_location
from NutanixAssignment.Utilities.OSHelper import FileSeparator


class DirectoryListing:

    @staticmethod
    def get_full_path(source, value):
        """
        Function works as os.path.join and returns absolute path
        :param source: String -> Path excluding last node File/Directory
        :param value: String -> Last Node File/Directory
        :return: String -> Absolute Path of the value Directory/File wrt to source
        """
        sep = FileSeparator.file_separator_pattern("posix")
        file_separator = sep.file_separator()
        return source + file_separator + value

    @staticmethod
    def listdir_fullpath(source):
        """
        This will return list of Files and Directories present in the path passed as param. Non recursive lisitng.
        :param source: Path of Directory for which list of Files/Directories is required
        :return: List -> Returns list of Files and Directories in the passed Directory
        """
        return [DirectoryListing.get_full_path(source, file_folder) for file_folder in listdir(source)]

    @staticmethod
    def list_all_files_and_directories_recursive_full_path(source):
        """
        This method returns recursive absolute path of files and folders present in the source directory or only source
        if it is a file
        :param source: String -> Source path whose recursive listing is required
        :return: List -> List of Files and Folders with there absolute path
        """
        list_of_files_folders = []
        try:
            if not isfile(source):
                list_of_files_folders = DirectoryListing.listdir_fullpath(source)
                try:
                    for listed_path in list_of_files_folders:
                        if not isfile(listed_path):
                            list_of_files_folders.extend(DirectoryListing.list_all_files_and_directories_recursive_full_path
                                                         (listed_path))
                except TypeError as err:
                    print(f"Type Error exception: {err}")
                except PermissionError as err:
                    print(f"File Permission exception: {err}")
            else:
                list_of_files_folders.append(source)
            return list_of_files_folders
        except FileNotFoundError as err:
            print(f"File/Folder Not Found exception: {err}")
            raise

    @staticmethod
    def list_all_files_and_directories_recursive_relative_path(source):
        """
        This method returns recursive relative path of files and folders wrt to source only source if it is a file
        :param source: String -> Source path whose recursive listing is required
        :return: List -> List of Files and Folders with there relative path
        """
        source = removing_unwanted_chars_in_folder_location(source)
        list_with_abs_path = DirectoryListing.list_all_files_and_directories_recursive_full_path(source)
        list_with_relative_path = [path.replace(source, "") for path in list_with_abs_path]
        return list_with_relative_path


if __name__ == '__main__':
    testCommonHelper = DirectoryListing()
    print(DirectoryListing.list_all_files_and_directories_recursive_full_path("/Users/arpit/Documents/Mac/Automation/cwa-mac-automation/WorkspaceAutomation/Webservice"))
    print(DirectoryListing.list_all_files_and_directories_recursive_relative_path("/Users/arpit/Documents/Mac/Automation/cwa-mac-automation/WorkspaceAutomation/Webservice"))
