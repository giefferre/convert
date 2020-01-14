from flask import Flask, request, jsonify
from werkzeug.exceptions import BadRequest, NotFound
from converter import Converter, ConverterRequest, ConverterResponse
from converter.rate_providers import ECBRateProvider
import logging


'''
The following inizialization could happen elsewhere and the dependency converter
could be passed using dependency injection, using tools such as
https://pypi.org/project/Flask-Injector/
'''
rp = ECBRateProvider()
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
        app.logger.debug(e)
        raise BadRequest(e)

    try:
        res = c.convert(req)
        return jsonify(res.serialize())
    except Exception as e:
        app.logger.debug(e)
        raise NotFound(e)


if __name__ == '__main__':
    app.run(host="0.0.0.0")
