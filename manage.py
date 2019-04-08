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

@app.route("/about")
def about():
    return render_template("About.html")


@app.route("/share", methods=["POST"])
def book():
    booktitle = request.form['booktitle']
    pages = request.form['pages']
    location = request.form['location']

    #return  'You have submitted %s which has  %s  pages <br/> <a href="/"> Back Home</a>' % (title, pages)
    return render_template("Share.html", booktitle=request.form["booktitle"], pages =request.form["pages"], location =request.form["location"])


@app.route("/books",)
def books():
    return  render_template("Books.html")







app.run(debug=True)
