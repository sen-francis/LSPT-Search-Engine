import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/get_config')
def get_config():
	try: 
		with open('config.json') as file:
	  		config = json.load(file)

		response = app.response_class(
			response = json.dumps(config),
			status = 200,
			mimetype = 'application/json'
		)
		return response
	except Exception as error:
		response = app.response_class(
			response = json.dumps({"error": "Could not load configuration"}),
			status = 500,
			mimetype = 'application/json'
		)
		return response

@app.route('/save_config', methods = ['POST'])
def save_config():
	json_content = request.get_json()

	stop_words_list = [word.strip() for word in json_content["stop_words"].split(',')]
	json_content["stop_words"] = stop_words_list;

	with open('config.json', 'w') as file:
		json.dump(json_content, file, indent = 4)

	response = app.response_class(
		response = json.dumps({}),
		status = 200,
		mimetype = 'application/json'
	)
	return response

