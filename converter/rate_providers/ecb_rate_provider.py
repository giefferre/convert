# -*- coding: utf-8 -*-

from .interface import RateProviderInterface
from datetime import datetime
import xml.etree.ElementTree as ET
import requests


class ECBRateProvider(RateProviderInterface):
    '''
    Provides currency exchange rates from European Central Bank.
    '''

    SOURCE_URL = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml'
    BASE_CURRENCY_CODE = 'EUR'

    def __init__(self):
        self._load_data_from_remote_endpoint()

    def get_rate(self, src_currency: str, dest_currency: str, reference_date: datetime) -> float:
        rates_per_day = self._get_rates_per_day(reference_date)

        if src_currency == self.BASE_CURRENCY_CODE:
            return self._get_rate(rates_per_day, dest_currency)

        eur_to_src_currency_rate = self._get_rate(rates_per_day, src_currency)
        eur_rate = 1 / eur_to_src_currency_rate

        if dest_currency == self.BASE_CURRENCY_CODE:
            return eur_rate

        return eur_rate * self._get_rate(rates_per_day, dest_currency)

    def _load_data_from_remote_endpoint(self):
        source_data = requests.get(self.SOURCE_URL)
        self._xml_namespace = {
            'd': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}
        self._xml_data = ET.fromstring(source_data.text)

    def _get_rates_per_day(self, reference_date: datetime) -> list:
        day_key = reference_date.strftime("%Y-%m-%d")
        nodes_per_day = self._xml_data.find("d:Cube", self._xml_namespace)

        for node in nodes_per_day:
            if node.get("time") == day_key:
                return list(node)
        raise Exception("reference_date not found")

    def _get_rate(self, rates_per_day: list, dest_currency: str) -> float:
        for node in rates_per_day:
            if node.get("currency") == dest_currency:
                return float(node.get("rate"))
        raise Exception("rate per currency %s not found" % dest_currency)
