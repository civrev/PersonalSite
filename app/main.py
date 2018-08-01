from sys import argv
from flask import Flask, render_template, url_for

from views.index import Index

#constructor for Flask object
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	#templates are considered by default in the /templates folder
	return render_template('index.html', **Index().dict)

@app.route('/bio')
def bio():
	return render_template('bio.html')

@app.route('/skills')
def skills():
	return render_template('skills.html')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/website')
def website():
	return render_template('website.html')

@app.route('/interact')
def interact():
	return render_template('interact.html')

@app.route('/contact')
def contact():
	return render_template('contact.html')

#hello world!
@app.route('/hw')
def hello_world():
	return 'Hello, World!'



if __name__ == '__main__':
	#when testing via command line, just add 'debug' at the end of running this file

	#'app' is the Flask() object we made at top
	app.run(debug = 'debug' in argv)