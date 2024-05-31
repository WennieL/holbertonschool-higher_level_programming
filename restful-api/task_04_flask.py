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
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    '''Add new user'''
    user_data = request.get_json()

    # Check if the 'username' field is missing
    if "username" not in user_data:
        return jsonify({"error": "Username is required"}), 400

    username = user_data.get("username")

    # Check if the username already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    # users[username] = user_data
    users[username] = {
        "username": username,
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")

    }
    return jsonify({"message": "User added", "User": users[username]}), 201


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
