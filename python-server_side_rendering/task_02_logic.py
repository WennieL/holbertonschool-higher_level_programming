#!/usr/bin/python3

from flask import Flask, render_template
import json

app = Flask(__name__)

app.static_folder = 'static'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    sites = ["twitter", "facebook", "instagram"]
    return render_template('about.html', sites=sites)


@app.route('/items')
def items():
    items_list = []

    with open("./items.json", "r", encoding="utf-8") as jfile:
        data = json.load(jfile)

    for key, value in data.items():
        items_list.extend(value)

    return render_template('items.html', items=items_list)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=3000)
