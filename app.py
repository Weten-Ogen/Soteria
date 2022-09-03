from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config["SECRET_KEY"]="minini"

@app.route('/home')
def index():
  flash('What is your Name')
  return render_template('index.html')

@app.route('/greet',methods=["POST", "GET"])
def greet():
  flash('Hello ' + str(request.form["name_input"]) + ", great to see you")
  return render_template('index.html')