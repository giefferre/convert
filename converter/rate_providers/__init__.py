# -*- coding: utf-8 -*-

"""
Offers different rate providers meant to be used with the converter package.
"""

from .interface import RateProviderInterface
from .random_provider import RandomRateProvider
from .ecb_rate_provider import ECBRateProvider
