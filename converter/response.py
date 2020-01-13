# -*- coding: utf-8 -*-


class ConverterResponse(object):
    def __init__(self, amount: float, currency_iso_4217: str):
        self._set_amount(amount)
        self._set_currency(currency_iso_4217)

    def _set_amount(self, amount: float):
        if not amount or amount < float(0):
            raise Exception("invalid amount provided %f" % amount)
        self._amount = amount

    def _set_currency(self, currency_iso_4217: str):
        self._currency = currency_iso_4217

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def serialize(self):
        return {
            'amount': self.amount,
            'currency': self.currency,
        }
