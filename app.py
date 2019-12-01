__author__ =['Anush Sankaran(anussank@in.ibm.com)', 'Raunak Sinha (rsinha05@in.ibm.com)']
__copyright__ = 'Copyright 2018, IBM Corp.'
__maintainer__ = ['Anush Sankaran', 'Raunak Sinha']
__email__ = ['anussank@in.ibm.com', 'rsinha05@in.ibm.com']
__status__ = "Production"

from flask import (Flask, Response, g, render_template, request, send_file,
				   send_from_directory)
from flask_cors import CORS
import os, json
from werkzeug.utils import secure_filename
import traceback
from agant import main

application = Flask(__name__ , template_folder='./public', static_folder='./public/static')
CORS(application)

application.config['UPLOAD_FOLDER'] = 'uploads/'
if not os.path.exists('uploads/'):
	os.mkdir('uploads/')

def init():
    return None

@application.route('/', methods=['GET'])
def index():
	return render_template("views/index.html")

@application.route('/temp_api', methods=['GET'])
def temp_api():
    print("reached here")
    import json
    data = {}
    data['people'] = []
    data['people'].append({
        'name': 'Scott',
        'website': 'stackabuse.com',
        'from': 'Nebraska'
    })
    data['people'].append({
        'name': 'Larry',
        'website': 'google.com',
        'from': 'Michigan'
    })
    data['people'].append({
        'name': 'Tim',
        'website': 'apple.com',
        'from': 'Alabama'
    })
    print("reached here 2")
    with open('agant/logs/data.txt', 'w') as outfile:
        json.dump(data, outfile)
    return json.dumps({"Success":True, "Errors":[]}), 200

@application.route('/gan_model', methods=['POST'])
def gan_model():
    response_json = {"Success":False, "Errors":[]}
    try:
        file = request.files['config_file']
        if file.filename == '':
            response_json["Errors"] = "Please provide the file"
            return json.dumps(response_json),500
        if file:
            filename = secure_filename(file.filename)
            data_path = os.path.join(application.config['UPLOAD_FOLDER'], filename)
            file.save(data_path)

        main.driver_gan_generation(data_path)
        response_json["Success"] = True
        return json.dumps(response_json), 200

    except Exception as e:
        send_error = traceback.format_exc()
        response_json["Errors"] = ["Sorry! we are not able to get data quality", send_error]
        return json.dumps(response_json),500

port = int(os.getenv('PORT', 7005))
hostname = '0.0.0.0'
if __name__ == "__main__":
	init()
	application.run(host=hostname, port=port, debug=False)
