#!/usr/bin/env python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    """ Returns some text. """
    return 'Hello World!'

@app.route('/search_user', methods=['POST'])
def search_user():
    q = request.form.get('q')
    if q:
        user = {
            'id': 1,
            'name': 'John Doe',
            'email': 'johndoe@example.com'
        }
        return jsonify(user)
    else:
        return jsonify({}), 400

if __name__ == '__main__':
    app.run(port=5000)

