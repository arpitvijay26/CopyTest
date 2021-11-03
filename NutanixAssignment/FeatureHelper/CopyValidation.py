# -*- encoding: utf-8 -*-


from NutanixAssignment.Utilities.DirectoryListing import DirectoryListing
from NutanixAssignment.Utilities.CommonHelper import FileSeparator, md5sum, isfile


class CopyValidator:
    """
    This class helps in validating whether copy functionality worked fine by providing 4 methods:
    1. List of files/folders that got copied from source to destination
    2. List of files which had integrity issue while getting copied.
    3. List of junk files/folders that got copied to Destination which are not in Source directory
    4. List of Files/Folders missing in Destination Directory which are there in Source Directory
    """

    def __init__(self, source, destination, os):
        self.source = source
        self.destination = destination
        self.list_of_source_files_folders = DirectoryListing.list_all_files_and_directories_recursive_relative_path(source)
        self.list_of_destination_files_folders = DirectoryListing.list_all_files_and_directories_recursive_relative_path(destination)
        self.file_separator_pattern = FileSeparator.file_separator_pattern(os)
        self.file_separator = self.file_separator_pattern.file_separator()

    def list_of_files_directories_copied(self):
        """
        We use set method to find intersection of files/folders between source and destination.
        :return: List -> List of files/folders present in both Source and Destination
        """
        list_of_files_directories = list(set(self.list_of_source_files_folders).intersection(self.list_of_destination_files_folders))
        # We are using set here as while running Set is faster then List Comprehension. Pros of Sets is Faster Speed and
        # Cons here is additional space requirement
        print(f"List of Files and Directories which were copied: {list_of_files_directories}")
        return list_of_files_directories

    def list_of_files_integrity_problem(self):
        """
        To test file integrity, we use list of files which are copied from source to destination and check there md5 are
        same or not. If not, we add them into list of files with integrity problem and return this list.
        :return: List -> List of files which have integrity issues
        """
        files_with_integrity_problem = []
        for file in self.list_of_files_directories_copied():
            if isfile(self.source + self.file_separator + file) and isfile(self.destination + self.file_separator + file):
                if not md5sum(self.source + self.file_separator + file) == \
                       md5sum(self.destination + self.file_separator + file):
                    files_with_integrity_problem.append(file)
        print(f"List of Files which have integrity issue: {files_with_integrity_problem}")
        return files_with_integrity_problem

    def list_of_junk_files_in_destinaton(self):
        """
        To find junk files in destination (additional files copied in destination which were not there in source), we
        take difference of set of destination with set of source files.
        :return: List -> List of files which are additionally present in Destination and are not in Source
        """
        list_of_junk_files_dest = list(set(self.list_of_destination_files_folders).difference(set(self.list_of_source_files_folders)))
        # We are using set here as while running Set is faster then List Comprehension. Pros of Sets is Faster Speed and
        # Cons here is additional space requirement
        print(f"List of Junk Files in Destination: {list_of_junk_files_dest}")
        return list_of_junk_files_dest

    def list_of_missing_files_in_destination(self):
        """
        To find files missing in destination (files in source which were not there in destination), we take difference
        of set of source with set of destination files.
        :return: List -> List of files which are present in Source and are not in Destination
        """
        list_of_missing_files = list(set(self.list_of_source_files_folders) - set(self.list_of_destination_files_folders))
        # We are using set here as while running Set is faster then List Comprehension. Pros of Sets is Faster Speed and Cons here is additional
        # space requirement
        print(f"List of Missing Files in Destination: {list_of_missing_files}")
        return list_of_missing_files


if __name__ == '__main__':
    copy_validator = CopyValidator("/Users/arpit/Documents/Mac/Automation/cwa-mac-automation/WorkspaceAutomation"
                                   "/Webservice", "/Users/arpit/Documents/Mac/Automation/cwa-mac-automation"
                                    "/WorkspaceAutomation/Webservice", "posix")
    print(copy_validator.list_of_files_integrity_problem())