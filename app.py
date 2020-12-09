"""
Text Transformation Service
---------------------------

The application has been developed as a service to transform a list of HTML documents
in parallel. The service is intended to run as a CRON job once every day and provides
a Administrative UI where settings related to the service can be tweaked and saved.

Developed by:
Team-P: Karan Bhanot, Tim Budding, Sen Francis and Zachary Koo
Last Updated on: December 9, 2020
"""

# Import libraries
import json
from itertools import islice
from flask import Flask, render_template, jsonify, request
from functions import getDocument


# Define app for FLASK
app = Flask(__name__)


@app.route('/')
def index():
	"""
	Renders the homepage `index.html` to view and change settings.
	"""

	return render_template('index.html')


@app.route('/test')
def test():
	"""
	Renders the test page `test.html` where admins can test the latest
	settings saved by them.
	"""

	return render_template('test.html')


@app.route('/get_config')
def get_config():
	"""
	Loads the current configuration and updates settings on the UI
	based on it.
	"""

	try: 
		# Read the file `config.json`
		with open('config.json') as file:
	  		config = json.load(file)

	  	# Create a response variable
		response = app.response_class(
			response = json.dumps(config),
			status = 200,
			mimetype = 'application/json'
		)

		# Send response
		return response

	except Exception as error:

		# Create response with error code 500 in case of an error
		response = app.response_class(
			response = json.dumps({"messagee": "ERROR: Could not load configuration."}),
			status = 500,
			mimetype = 'application/json'
		)

		# Send error response
		return response


@app.route('/save_config', methods = ['POST'])
def save_config():
	"""
	Saves the configuration to the `config.json` file based on what 
	the admin selected as the values.
	"""

	try:
		# Read the request data and create proper json format from it
		json_content = request.get_json()
		stop_words_list = [word.strip() for word in json_content["stop_words"].split(',')]
		json_content["stop_words"] = stop_words_list;

		# Write it to the `config.json` file
		with open('config.json', 'w') as file:
			json.dump(json_content, file, indent = 4)

		# Create resonse to tell that the settings were updated
		response = app.response_class(
			response = json.dumps({"message": "Settings updated."}),
			status = 200,
			mimetype = 'application/json'
		)

		# Send response
		return response

	except Exception as error:

		# Create resonse to tell that the settings were not updated
		response = app.response_class(
			response = json.dumps({"message": "ERROR: Could not update settings."}),
			status = 500,
			mimetype = 'application/json'
		)

		# Send error response
		return response


@app.route('/test_config', methods = ['POST'])
def test_config():
	"""
	Applies the last stored text transformation configuration
	to the content sent by the admin.
	"""

	try:
		# Read the content
		json_content = request.get_json()
		to_transform = json_content['to_transform']

		# Transform the HTML in the URL
		result_json = getDocument(to_transform)

		# Filter data based on settings
		with open('config.json') as file:
	  		config = json.load(file)

	  	# Remove links if setting is off
		if config["links"] == 0:
	  		del result_json["url"]
		else:
	  		result_json["links"] = result_json["url"][:10]
	  		del result_json["url"]

	  	# Show top 10 unqiue words
		result_json["unique_words"] = result_json["Ngram Counts"][0]
		result_json["unique_words"] = dict(islice(result_json["unique_words"].items(), 10))

		# Show top 10 bi-grams if setting is on
		if config["bi_gram"] == 1:
	  		result_json["unique_bi_grams"] = result_json["Ngram Counts"][1]
	  		result_json["unique_bi_grams"] = dict(islice(result_json["unique_bi_grams"].items(), 10))

	  	# Show top 10 tri-grams if setting is on
		if config["tri_gram"] == 1:
	  		result_json["unique_tri_grams"] = result_json["Ngram Counts"][2]
	  		result_json["unique_tri_grams"] = dict(islice(result_json["unique_tri_grams"].items(), 10))

	  	# Remove extra JSON content before sending
		del result_json["Ngram Counts"]

		# Create response with the transformed text
		response = app.response_class(
			response = json.dumps({"message": "Text transformed.", "transformed_text": result_json}),
			status = 200,
			mimetype = 'application/json'
		)

		# Send response
		return response

	except Exception as error:

		# Create response with error
		response = app.response_class(
			response = json.dumps({"message": "ERROR: Could not transform text."}),
			status = 500,
			mimetype = 'application/json'
		)

		# Send error response
		return response	

