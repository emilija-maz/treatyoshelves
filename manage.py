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
def email ():
    form_data=request.form
    print form_data["email"]
    requests.post(
        "https://api.mailgun.net/v3/sandbox2da01c53ab0b4d2597aae47c7a5e477f.mailgun.org/messages",
        auth=("api", "9e8dc86bae0e2701c4f8742169e2e9b2-7caa9475-44465c9e"),
        data={"from": "Excited User <mailgun@sandbox2da01c53ab0b4d2597aae47c7a5e477f.mailgun.org>",
            "to": ["rkag@st-andrews.ac.uk", "kl96@st-andrews.ac.uk"],
            "subject": "Hello",
            "text": "Testing some Mailgun awesomness!"})
    return "Thank you!"


app.run(debug=True)
