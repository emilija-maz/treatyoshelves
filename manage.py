from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("landingpage.html")

@app.route("/<name>")
def hello_name(name):
	return render_template("Search.html", name = name.title())
	# by default it checks templates folder
	# if name = None => it will say hello anonymous person

# @app.route("/")
# def serve_index():
# 	return render_template("email.html")
@app.route('/search')
def search():
	return render_template("Search.html")

@app.route("/email", methods=["POST"])
def email():
	form_data = request.form
	print form_data["email"]
	requests.post(
		"https://api.mailgun.net/v3/sandboxf8a60abf48434795bd9e0fee08a8494f.mailgun.org/messages",
        auth=("api", "f901c98b1d9032490412503076633c44-acb0b40c-e4f0c684"),
        data={"from": " Your past self <mailgun@sandboxf8a60abf48434795bd9e0fee08a8494f.mailgun.org>",
              "to": ["emilijamazuraite@gmail.com"],
              "subject": "This is a test, don't panic",
              "text": "Hi" +  form_data["name"] +"I am testing a flask file!"}
		)
              # "Hi {}, this is an email".format(form_data["name"])
	return "All OK cool"



app.run(debug=True)

