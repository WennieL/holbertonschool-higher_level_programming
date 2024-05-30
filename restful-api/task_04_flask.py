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
    user_data = request.get_json()
    username = user_data.get("username")
    if not username:
        return ({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "username": user_data.get("username"),
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }

    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(debug=True)
