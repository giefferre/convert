# -*- coding: utf-8 -*-

import mock
import unittest
from . import ECBRateProvider
from datetime import datetime


class TestECBRateProvider(unittest.TestCase):
    def test_get_rate_raises_exception(self):
        with mock.patch('requests.get', self._mock_requests_get):
            sut = ECBRateProvider()

            test_cases = [
                ["EUR", "USD", "2020-01-10"],
                ["SSS", "EUR", "2020-01-08"],
            ]

            for test_case in test_cases:
                with self.assertRaises(Exception):
                    sut.get_rate(test_case[0], test_case[1], datetime.strptime(test_case[2], "%Y-%m-%d"))

    def test_get_rate(self):
        with mock.patch('requests.get', self._mock_requests_get):
            sut = ECBRateProvider()

            test_cases = [
                ["EUR", "USD", "2020-01-08", 1.1115],
                ["USD", "EUR", "2020-01-08", 0.899685110211426],
                ["USD", "CAD", "2020-01-08", 1.3018443544759335],
            ]

            for test_case in test_cases:
                rate = sut.get_rate(test_case[0], test_case[1], datetime.strptime(test_case[2], "%Y-%m-%d"))
                self.assertEqual(test_case[3], rate)

    def _mock_requests_get(self, url):
        return MockRequestsResponse('''<?xml version="1.0" encoding="UTF-8"?>
<gesmes:Envelope xmlns:gesmes="http://www.gesmes.org/xml/2002-08-01" xmlns="http://www.ecb.int/vocabulary/2002-08-01/eurofxref"><gesmes:subject>Reference rates</gesmes:subject><gesmes:Sender><gesmes:name>European Central Bank</gesmes:name></gesmes:Sender><Cube>
<Cube time="2020-01-08"><Cube currency="USD" rate="1.1115"/><Cube currency="JPY" rate="120.86"/><Cube currency="BGN" rate="1.9558"/><Cube currency="CZK" rate="25.265"/><Cube currency="DKK" rate="7.4731"/><Cube currency="GBP" rate="0.84868"/><Cube currency="HUF" rate="331.08"/><Cube currency="PLN" rate="4.2429"/><Cube currency="RON" rate="4.7774"/><Cube currency="SEK" rate="10.5108"/><Cube currency="CHF" rate="1.0792"/><Cube currency="ISK" rate="137.1"/><Cube currency="NOK" rate="9.8508"/><Cube currency="HRK" rate="7.449"/><Cube currency="RUB" rate="68.6389"/><Cube currency="TRY" rate="6.6158"/><Cube currency="AUD" rate="1.6195"/><Cube currency="BRL" rate="4.5092"/><Cube currency="CAD" rate="1.447"/><Cube currency="CNY" rate="7.7184"/><Cube currency="HKD" rate="8.6424"/><Cube currency="IDR" rate="15441.51"/><Cube currency="ILS" rate="3.8541"/><Cube currency="INR" rate="79.709"/><Cube currency="KRW" rate="1297.37"/><Cube currency="MXN" rate="20.9079"/><Cube currency="MYR" rate="4.5588"/><Cube currency="NZD" rate="1.6739"/><Cube currency="PHP" rate="56.42"/><Cube currency="SGD" rate="1.5014"/><Cube currency="THB" rate="33.74"/><Cube currency="ZAR" rate="15.8166"/></Cube>
</Cube></gesmes:Envelope>
''')


class MockRequestsResponse(object):
    def __init__(self, content):
        self._content = content

    @property
    def text(self):
        return self._content
