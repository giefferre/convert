# -*- coding: utf-8 -*-

from datetime import datetime

class RateProviderInterface(object):
    def get_rate(self, src_currency: str, dest_currency: str, reference_date: datetime) -> float:
        raise NotImplementedError
