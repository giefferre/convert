# -*- coding: utf-8 -*-

import unittest
from converter import Converter, ConverterRequest, ConverterResponse
from datetime import datetime

from .rate_providers import RateProviderInterface


class TestConverter(unittest.TestCase):
    def test_constructor_raises_when_invalid_rate_provider_is_given(self):
        with self.assertRaises(Exception):
            Converter("not a RateProvider")

    def test_convert(self):
        sut = Converter(MockRateProvider())

        test_cases = [
            [15.0, "EUR", "EUR", "2020-01-13", ConverterResponse(15.0, "EUR")],
            [15.0, "EUR", "USD", "2020-01-14", ConverterResponse(30.0, "USD")],
        ]

        for test_case in test_cases:
            req = ConverterRequest(
                test_case[0],
                test_case[1],
                test_case[2],
                test_case[3],
            )
            res = sut.convert(req)
            self.assertEqual(test_case[4].serialize(), res.serialize())


class MockRateProvider(RateProviderInterface):
    def get_rate(self, src_currency: str, dest_currency: str, reference_date: datetime) -> float:
        return 2.0
