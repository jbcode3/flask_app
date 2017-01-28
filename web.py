from flask import Flask, render_template, request #imort flask and render template and request
import weather
import os
app = Flask(__name__)    #create a variable

@app.route("/")          #this creates a page
#def hello():             #create a function
    #return "Hello World!" #function returns hello world
def index(): #create a function
	address = request.values.get('address')     #this will go into the parameters and get whatever is in there and pass it to name.         
	forecast = None
	if address:
		forecast = weather.get_weather(address)
	return render_template('index.html', forecast=forecast)
	
@app.route('/about')       #this creates an about page
def about():
		return render_template('about.html')

if __name__ == "__main__": #these 2 lines tell the application to run
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)