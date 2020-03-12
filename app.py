from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
	# here we use 'render_template' to link to the html template
	return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
