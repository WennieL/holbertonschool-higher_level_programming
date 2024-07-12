#!/usr/bin/python3

from flask import Flask, render_template, request
from pathlib import Path
import json
import csv
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

    # json to python -> readable to items.html
    with open("./task_02/items.json", "r", encoding="utf-8") as jfile:
        data = json.load(jfile)

    for key, value in data.items():
        items_list.extend(value)

    return render_template('items.html', items=items_list)


@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    data = []
    if source == "json":
        data = load_json_data("data/products.json", id)
    elif source == "csv":
        data = load_csv_data("data/products.csv", id)

    return render_template('product_display.html', data=data, source=source, id=id)


def load_json_data(filename, wanted_id=None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r', encoding="utf-8") as f:
            rows = json.load(f)
        for row in rows:
            key = row['id']

            if (wanted_id is not None and key == wanted_id) or (wanted_id is None):
                product = {}
                for k, v in row.items():
                    product[k] = v
                data.append(product)

    except ValueError as exc:
        raise ValueError(
            "Unable to load data from file '{}'".format(filename)) from exc

    return data


def load_csv_data(filename, wanted_id=None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r', encoding="utf-8") as csvfile:
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except ValueError as exc:
        raise ValueError(
            "Unable to load data from file '{}'".format(filename)) from exc

    return data


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(host="localhost", debug=True, port=3000)
