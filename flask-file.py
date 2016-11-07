import requests
from requests.auth import HTTPBasicAuth
from twilio.rest import TwilioRestClient
from flask import Flask, render_template, request 
from configobj import ConfigObj 

app = Flask(__name__)

@app.route('/') 
@app.route('/<name>')  
def home(name=None):
	return render_template('home.html', name=name)

@app.route('/message', methods=['GET', 'POST'])
def message():
		if request.method == 'GET':
			return render_template('message.html')
		else:
			number = request.form['phoneNumber']
			message = request.form['message']

			client = TwilioRestClient("ACa036fa9f0ec63a45c21007c829bb683a", "457bea6ca22b9218c11d4e488cbbdf55")

			message = client.messages.create(body=message, 
				to="+1"+number,
				from_="+15123944433") #replace with your own number

			return render_template('message.html', 
				success="You sent a bloody message.")

if __name__ == '__main__':
	app.run()
