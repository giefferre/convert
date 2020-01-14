# -*- coding: utf-8 -*-

from datetime import datetime

from .request import ConverterRequest
from .response import ConverterResponse
from .rate_providers import RateProviderInterface


class Converter(object):
    def __init__(self, rate_provider: RateProviderInterface):
        self._set_rate_provider(rate_provider)

    def convert(self, req: ConverterRequest) -> ConverterResponse:
        '''
        Converts the currency amount provided in the given ConverterRequest
        into the destination currency, returning a ConverterResponse object.
        '''

        multiplier = self._get_multiplier(
            req.src_currency, req.dest_currency, req.reference_date)
        converted_amount = req.amount * multiplier

        return ConverterResponse(converted_amount, req.dest_currency)

    def _get_multiplier(self, src_currency: str, dest_currency: str, reference_date: datetime) -> float:
        '''
        Returns:
        - 1.0 if source and destination currencies match, or
        - the exchange rate provided by the rate_provider
        '''

        if src_currency == dest_currency:
            return 1.0
        return self.rate_provider.get_rate(src_currency, dest_currency, reference_date)

    def _set_rate_provider(self, rate_provider: RateProviderInterface):
        get_rate_method = getattr(rate_provider, "get_rate", None)
        if not callable(get_rate_method):
            raise Exception(
                "invalid rate_provider given, does not implement get_rate method")
        self._rate_provider = rate_provider

    @property
    def rate_provider(self):
        return self._rate_provider
