#Software "cp" takes two argument. src -> Source location , dst -> DestinationLocation.
#"cp" copies all content of src ->dst.
#Syntax -> cp src dst


#As a part of QA, we need to validate if all the content of src is properly copied to dst. WRITE AUTOMATION FOR BELOW VALIDATION :
#And this includes 4 main aspects to validate :
#- All files/dirs copied
#- Data integrity maintained - list of corrupt files/dirs
#- Is there any junk (file/dir) copied in dst
#- Any missing file/dir in dst
#Use below helper methods to implement solution. DO NOT USE ANY additional libraries i.e do not import anything other than below methods in your solution.


#Helper methods (DO NOT IMPLEMENT THESE METHODS. THESE ARE AVAILABLE FOR YOU TO USE)
#-listdir(location) -> [files & dirs in current dir] (no recursive listing)
#-isfile(location) -> bool - True if file else False
#-md5sum(location) -> String - md5sum of file.


#Few tips :
#Try to build a skeleton code for modularised framework .
#Build atleast one method which can give all above result.

#Additional things to do :
#Provide rest API to trigger the test & get all 4 results separately

# System Requirements:
Python Requirements: Python 3.7 and above
OS Requirements: Tested on macos. Should work on Linux/Unix platform. Not tested on Windows.

# How to Run:
From cmdline:
  On Terminal run command:
  export FLASK_APP=RestAPI
  flask run
From IDE like Pycharm:
  Open RestAPI file in IDE and it has a main section. You can run from it.
  
# Run Using API: To run using WebBrowser or Postman, API to use:
#http://localhost:8080/testcopy?os=<os_name>&source=<source_folder_absolute_path>&destination=<destination_folder_absolute_path>
  
# Test using Code:
Run APICaller.py file. It will ask for location of json file. Provide the absolute path to json file and test will be run.
JSON format should be same as NutanixAssignment/TestFolder/test_using_api.json file

# Code Structure
NutanixAssignment
|
  Utilities: This has utility functions which can be used for test project.
  |
    OSHelper: It has OSHelper which is a factory pattern for running across different os. 
    Constant: Constant file will contain constants which can be used in project.
    CommonHelper: It contains dummy implementation of isfile, listdir and md5sum functions and some other helper functions.
    DirectoryListing: Using this class, we can get absolute and relative recursive listing of the folder.
  |
  FeatureHelper:
    CopyValidation: This contains CopyValidation class which will have reusable functions to validate copy functionality like files copied, file integrity issue,       files missing in destination and junk files in destination.
  |
  Test:
    TestCopyFunctionality: This contains test class which will test all 4 functionality and return a tuple containing list of files copied, file integrity issue,       files missing in destination and junk files in destination
  |
  TestFolder:
    This contains json file which we can supply to Test class and cover all 4 scenarios.
  |
  API:
    RestAPI: This will expose the API which will be used to call Test
    APICaller: This will contain code to call RestAPI and get list of 4 scenarios.

