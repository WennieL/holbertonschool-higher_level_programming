#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)


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
def users_specific(username):
    ''' User details endpoint'''
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    '''Add new user'''
    req_data = request.get_json()
    if not req_data:
        return jsonify({"error": "Not a JSON file"}), 400

    username = req_data.get("username")
    # Check if the 'username' field is missing
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if the username already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    user_data = {
        "name": req_data.get("name"),
        "age": req_data.get("age"),
        "city": req_data.get("city")
    }
    users[username] = user_data

    return jsonify({"message": "User added", "User": user_data}), 201


if __name__ == "__main__":
    app.run(debug=True)
