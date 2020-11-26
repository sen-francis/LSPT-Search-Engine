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

@app.route('/save_config', methods=['POST'])
def save_config():
	print(request.get_json())

	response = app.response_class(
		response = json.dumps({}),
		status = 200,
		mimetype = 'application/json'
	)
	return response

