# -*- coding: utf-8 -*-

from datetime import datetime
import random

from .interface import RateProviderInterface


class RandomRateProvider(RateProviderInterface):
    def get_rate(self, src_currency: str, dest_currency: str, reference_date: datetime) -> float:
        return random.uniform(1.0, 2.0)
