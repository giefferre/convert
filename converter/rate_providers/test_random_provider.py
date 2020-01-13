# -*- coding: utf-8 -*-

import unittest
from . import RandomRateProvider


class TestRandomRateProvider(unittest.TestCase):
    def test_get_rate_returns_different_results(self):
        sut = RandomRateProvider()

        mock_src_currency = "EUR"
        mock_dest_currency = "USD"
        mock_reference_date = "2020-01-11"

        first_result = sut.get_rate(mock_src_currency, mock_dest_currency, mock_reference_date)
        second_result = sut.get_rate(mock_src_currency, mock_dest_currency, mock_reference_date)

        self.assertNotEqual(first_result, second_result)