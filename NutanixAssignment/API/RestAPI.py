from flask import Flask, request, json
from NutanixAssignment.Utilities import Constant
from NutanixAssignment.Test.TestCopyFunctionality import TestCopy

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Simple web service call to check if webservice is up"""
    return "Webservice is running"


@app.route('/testcopy', methods=['GET', 'POST'])
def test_copy_func():
    """
        This function will reserve any free user available in Database.
        URL Format: http://<machine-ip>/testcopy?os=<os-type>&source=<source-directory>&destination=<destination-directory>
    """
    try:
        platform = request.args.get('os')
        if platform not in Constant.supported_platform:
            print(f'Specified Platform {platform} is not supported. Returning error Code 403.')
            return f'Specified Platform {platform} is not supported', 403
        source_location = request.args.get('source')
        destination_location = request.args.get('destination')
        if source_location != None and destination_location != None:
            print(f"Source Location is: {source_location}")
            print(f"Destination Location is: {destination_location}")
            test_copy = TestCopy(source_location, destination_location, platform)
            val = test_copy.test_copy_worked_correctly()
            print(f"Files copied from source to destination: {val[0]}")
            print(f"Junk Files in destination not available in source: {val[1]}")
            print(f"Files missing in destination but are present in source: {val[2]}")
            print(f"Files with integrity issue: {val[3]}")
            response = create_json(val)
            if response:
                return response, 200
            else:
                return f"Problem in sending response: 500", 500
        else:
            return f"Source and Destination need to be defined. Source/Destination Null Error: 400", 400
    except Exception as err:
        return f"API not responding: 404", 404

def create_json(a):
    dict = {
        "List of Copied Files and Folders": a[0],
        "List of Files with Integrity Problem": a[3],
        "List of Extra Files in Destination": a[2],
        "List of Missing Files in Destination": a[1]
    }
    return json.dumps(dict, indent = 4)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
