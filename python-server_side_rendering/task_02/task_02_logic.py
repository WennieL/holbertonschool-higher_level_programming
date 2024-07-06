#!/usr/bin/python3

from flask import Flask, render_template
import json
import os

# Path to the shared templates directory
template_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'templates'))

# Path to the shared static directory
static_dir = os.path.abspath(os.path.join(
    os.path.dirname(__file__), '..', 'static'))

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


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

    with open("./task_02/items.json", "r", encoding="utf-8") as jfile:
        data = json.load(jfile)

    for key, value in data.items():
        items_list.extend(value)

    return render_template('items.html', items=items_list)


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=3000)
