#!/usr/bin/python3

from flask import Flask, render_template

app = Flask(__name__)

app.static_folder = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    sites = ["twitter", "facebook", "instagram"]
    return render_template('about.html', sites=sites)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=3000)
