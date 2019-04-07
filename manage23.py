

from flask import Flask, render_template, request

app = Flask("My")

@app.route('/share')
def index():
    return render_template('Share.html')

@app.route('/share', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return 'Hello %s %s have fun learning python <br/> <a href="/share"> Back Home</a>' % (first_name, last_name)


app.run(host = '0.0.0.0', port = 3000)