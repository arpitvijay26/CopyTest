"""
API Caller functionality which uses request module to call testcopy api. This uses json file as a parameter
"""


import requests, json


def api_caller(json_file):
    try:
        with open(json_file, "r") as fp:
            test_data = json.load(fp)
            for data in test_data:
                response = requests.get("http://localhost:8080/testcopy", test_data[data])
                if response.status_code == 200:
                    print(response.text)
                else:
                    print(response.status_code)
    except (FileNotFoundError, PermissionError, TypeError) as err:
        print(f"Exception caught while accessing json file: {err}")
        raise


if __name__ == '__main__':
    json_file_path = input("Enter absolute file path of json file which contains test data:")
    api_caller(json_file_path)