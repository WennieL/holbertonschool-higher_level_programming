#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    '''prints welcoming message'''
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    '''Return JSON data'''
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    ''' Prints OK '''
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    ''' User details endpoint'''
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    '''Add new user'''
    user_data = request.json
    username = user_data.get("username")

    # users[username] = user_data
    users[username] = {
        "username": username,
        "name": user_data["name"],
        "age": user_data["age"],
        "city": user_data["city"]

    }
    return jsonify({"message": "User added", "User": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
