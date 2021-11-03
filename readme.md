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
#Python Requirements: Python 3.7 and above
#OS Requirements: Tested on macos. Should work on Linux/Unix platform. Not tested on Windows.

# How to Run:
#From cmdline:
  #On Terminal run command:
  #export FLASK_APP=RestAPI
  #flask run
#From IDE like Pycharm:
  #Open RestAPI file in IDE and it has a main section. You can run from it.
# Run Using API: To run using WebBrowser or Postman, API to use:
#http://localhost:8080/testcopy?os=<os>&source=<source_folder_absolute_path>&destination=<destination_folder_absolute_path>
# Test using Code:
#Run APICaller.py file. It will ask for location of json file. Provide the absolute path to json file and test will be run.
#JSON format should be same as NutanixAssignment/TestFolder/test_using_api.json file

