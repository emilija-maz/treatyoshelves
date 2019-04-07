from flask import Flask, render_template, request
import requests

app = Flask("MyApp")

@app.route("/")
def hello():
	return render_template("landingpage.html")


@app.route('/search')
def search():
    return render_template("Search.html")


@app.route('/share')
def share():
    return render_template("Share.html")

@app.rout("/about")
def about():
    return render_template("About.html")

app.run(debug=True)
