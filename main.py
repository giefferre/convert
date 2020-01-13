from flask import Flask, request, jsonify, abort, escape
from werkzeug.exceptions import BadRequest

app = Flask(__name__)


@app.route('/convert', methods=['GET'])
def convert():
    return jsonify({
        "amount": 12.34,
        "currency": "EUR"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0")
