from flask import Flask, request, json
from NutanixAssignment.Utilities import Config
from NutanixAssignment.Test.TestCopyFunctionality import TestCopy

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Simple web service call to check if webservice is up"""
    return "Webservice is running"


@app.route('/testcopy', methods=['GET', 'POST'])
def test_copy_func():
    """
        This function will test copy functionality.
        URL Format: http://<machine-ip>/testcopy?os=<os-type>&source=<source-directory>&destination=<destination-directory>
        """
    try:
        platform = request.args.get('os')
        if platform not in Config.supported_platform:
            print(f'Specified Platform {platform} is not supported. Returning error Code 403.')
            return f'Specified Platform {platform} is not supported', 403
        source_location = request.args.get('source')
        destination_location = request.args.get('destination')
        test_copy = TestCopy(source_location, destination_location, platform)
        val1, val2, val3, val4 = test_copy.validate_if_copy_worked_fine()
        response = create_json("val1", "val2", "val3", "val4")
        print(response)
        if response:
            return response, 200
        else:
            return f'All users reserved. Try again after sometime', 404
    except Exception as err:
        return f"Some issue in performing operation on API"

def create_json(a, b, c, d):
    dict = {
        "List of Copied Files and Folders": a,
        "List of Files with Integrity Problem": b,
        "List of Extra Files in Destination": c,
        "List of Missing Files in Destination": d
    }
    print(dict)
    return json.dumps(dict, indent = 4)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
