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

print "What's your api?"
api = raw_input()
print "Thank you {}".format(api)



@app.route("/email", methods=["POST"])
def email ():
    form_data=request.form
    print form_data["email"]
    requests.post(
        "https://api.mailgun.net/v3/sandbox2da01c53ab0b4d2597aae47c7a5e477f.mailgun.org/messages",
        auth = ("api", "{}".format(api)),
        data={"from": "Treat yo shelves <mailgun@sandbox2da01c53ab0b4d2597aae47c7a5e477f.mailgun.org>",
            "to": [form_data["email"]],
            "subject": "Are you ready to Treat yo shelves?",
            "text": "Hello! Thanks for signing up and letting us know your whereabouts. You will shortly be allocated a book which will be posted to you! We'll be in touch. The Treat yo selves team"})
    return "Thank you! Get back to the home page here:"





app.run(debug=True)
