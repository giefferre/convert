# -*- coding: utf-8 -*-

import unittest
from datetime import datetime
from converter import ConverterRequest


class TestConverterRequest(unittest.TestCase):
    def test_constructor_raises_when_invalid_data_provided(self):
        test_cases = [
            ["not a float", "EUR", "USD", "2020-01-12"],
            [-1.0, "EUR", "USD", "2020-01-12"],
            [1.0, "invalid source currency", "USD", "2020-01-12"],
            [1.0, "EUR", "invalid dest currency", "2020-01-12"],
            [1.0, "EUR", "USD", "not a date"],
            [1.0, "EUR", "USD", "2030-01-12"],  # date in the future!
        ]

        for test_case in test_cases:
            self._execute_test_raises(test_case[0], test_case[1],
                                      test_case[2], test_case[3])

    def test_constructor_completes_successfully(self):
        sut = ConverterRequest(1.0, "EUR", "USD", "2020-01-12")
        self.assertEqual(1.0, sut.amount)
        self.assertEqual("EUR", sut.src_currency)
        self.assertEqual("USD", sut.dest_currency)
        self.assertEqual(datetime.strptime(
            "2020-01-12", "%Y-%m-%d"), sut.reference_date)

    def _execute_test_raises(self, amount, src, dest, date):
        with self.assertRaises(Exception):
            ConverterRequest(amount, src, dest, date)
