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



app.run(debug=True)
