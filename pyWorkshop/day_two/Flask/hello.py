from flask import Flask
app = Flask(__name__) #app flask object, instantiated with dunder name
#we will add decorater to specify routes

@app.route("/")
def hello_world():
	return "hello_world"

