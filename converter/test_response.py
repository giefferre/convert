# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
from converter import ConverterResponse


class TestConverterResponse(unittest.TestCase):
    def test_constructor_raises_when_invalid_data_provided(self):
        test_cases = [
            ["not a float", "EUR"],
            [-1.0, "EUR"],
        ]

        for test_case in test_cases:
            self._execute_test_raises(test_case[0], test_case[1])

    def test_constructor_completes_successfully(self):
        sut = ConverterResponse(12.34, "EUR")
        self.assertEqual(12.34, sut.amount)
        self.assertEqual("EUR", sut.currency)
    
    def test_serialize(self):
        sut = ConverterResponse(12.34, "EUR")
        expected_object = {
            "amount": 12.34,
            "currency": "EUR"
        }
        self.assertEqual(expected_object, sut.serialize())

    def _execute_test_raises(self, amount, currency):
        with self.assertRaises(Exception):
            ConverterResponse(amount, currency)
