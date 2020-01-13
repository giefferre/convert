from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest
from converter import Converter, ConverterRequest, ConverterResponse
from converter.rate_providers import RandomRateProvider


'''
The following inizialization could happen elsewhere and the dependency converter
could be passed using dependency injection, using tools such as
https://pypi.org/project/Flask-Injector/
'''
rp = RandomRateProvider()
c = Converter(rp)

app = Flask(__name__)

@app.route('/convert', methods=['GET'])
def convert():
    try:
        req = ConverterRequest(
            float(request.args.get('amount')),
            request.args.get('src_currency'),
            request.args.get('dest_currency'),
            request.args.get('reference_date'),
        )
    except Exception as e:
        raise BadRequest(e)

    res = c.convert(req)

    return jsonify(res.serialize())


if __name__ == '__main__':
    app.run(host="0.0.0.0")
