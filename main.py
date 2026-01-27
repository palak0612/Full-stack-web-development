'''from flask import Flask, render_template, redirect, url_for
#call the html page- render template
app = Flask(__name__)

@app.route("/") #checks the url 
def home():
    #return "hey this is first line of first page"
    return redirect((url_for("index")))

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True) '''
    
from flask import Flask, render_template, url_for, redirect,request, session
app = Flask(__name__)

@app.route('/')
def home():
  return redirect((url_for("index")))

@app.route('/index')
def index():
  return render_template("index.html")

if(__name__) == "__main__":
   app.run(debug = True) 