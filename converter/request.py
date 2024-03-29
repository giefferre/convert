# -*- coding: utf-8 -*-

from datetime import datetime


class ConverterRequest(object):

    """
    List of valid currencies from the official ISO website.
    https://www.iso.org/iso-4217-currency-codes.html

    This list has been considered static as the list doesn't change too often.
    """
    VALID_CURRENCIES = [
        "ADP", "AED", "AFA", "AFN", "ALK", "ALL", "AMD", "ANG", "AOA", "AOK",
        "AON", "AOR", "ARA", "ARP", "ARS", "ARY", "ATS", "AUD", "AWG", "AYM",
        "AZM", "AZN", "BAD", "BAM", "BBD", "BDT", "BEC", "BEF", "BEL", "BGJ",
        "BGK", "BGL", "BGN", "BHD", "BIF", "BMD", "BND", "BOB", "BOP", "BOV",
        "BRB", "BRC", "BRE", "BRL", "BRN", "BRR", "BSD", "BTN", "BUK", "BWP",
        "BYB", "BYN", "BYR", "BZD", "CAD", "CDF", "CHC", "CHE", "CHF", "CHW",
        "CLF", "CLP", "CNX", "CNY", "COP", "COU", "CRC", "CSD", "CSJ", "CSK",
        "CUC", "CUP", "CVE", "CYP", "CZK", "DDM", "DEM", "DJF", "DKK", "DOP",
        "DZD", "ECS", "ECV", "EEK", "EGP", "ERN", "ESA", "ESB", "ESP", "ETB",
        "EUR", "FIM", "FJD", "FKP", "FRF", "GBP", "GEK", "GEL", "GHC", "GHP",
        "GHS", "GIP", "GMD", "GNE", "GNF", "GNS", "GQE", "GRD", "GTQ", "GWE",
        "GWP", "GYD", "HKD", "HNL", "HRD", "HRK", "HTG", "HUF", "IDR", "IEP",
        "ILP", "ILR", "ILS", "INR", "IQD", "IRR", "ISJ", "ISK", "ITL", "JMD",
        "JOD", "JPY", "KES", "KGS", "KHR", "KMF", "KPW", "KRW", "KWD", "KYD",
        "KZT", "LAJ", "LAK", "LBP", "LKR", "LRD", "LSL", "LSM", "LTL", "LTT",
        "LUC", "LUF", "LUL", "LVL", "LVR", "LYD", "MAD", "MDL", "MGA", "MGF",
        "MKD", "MLF", "MMK", "MNT", "MOP", "MRO", "MTL", "MTP", "MUR", "MVQ",
        "MVR", "MWK", "MXN", "MXP", "MXV", "MYR", "MZE", "MZM", "MZN", "NAD",
        "NGN", "NIC", "NIO", "NLG", "NOK", "NPR", "NZD", "OMR", "PAB", "PEH",
        "PEI", "PEN", "PES", "PGK", "PHP", "PKR", "PLN", "PLZ", "PTE", "PYG",
        "QAR", "RHD", "ROK", "ROL", "RON", "RSD", "RUB", "RUR", "RWF", "SAR",
        "SBD", "SCR", "SDD", "SDG", "SDP", "SEK", "SGD", "SHP", "SIT", "SKK",
        "SLL", "SOS", "SRD", "SRG", "SSP", "STD", "SUR", "SVC", "SYP", "SZL",
        "THB", "TJR", "TJS", "TMM", "TMT", "TND", "TOP", "TPE", "TRL", "TRY",
        "TTD", "TWD", "TZS", "UAH", "UAK", "UGS", "UGW", "UGX", "USD", "USN",
        "USS", "UYI", "UYN", "UYP", "UYU", "UZS", "VEB", "VEF", "VNC", "VND",
        "VUV", "WST", "XAF", "XAG", "XAU", "XBA", "XBB", "XBC", "XBD", "XCD",
        "XDR", "XEU", "XFO", "XFU", "XOF", "XPD", "XPF", "XPT", "XRE", "XSU",
        "XTS", "XUA", "XXX", "YDD", "YER", "YUD", "YUM", "YUN", "ZAL", "ZAR",
        "ZMK", "ZMW", "ZRN", "ZRZ", "ZWC", "ZWD", "ZWL", "ZWN", "ZWR",
    ]
    DEFAULT_CURRENCY = "EUR"

    def __init__(self, amount: float, src_currency_iso_4217: str, dest_currency_iso_4217: str, date_iso_8601: str):
        self._set_amount(amount)
        self._set_src_currency(src_currency_iso_4217)
        self._set_dest_currency(dest_currency_iso_4217)
        self._set_reference_date(date_iso_8601)

    def _set_amount(self, amount: float):
        if not amount or amount < float(0):
            raise Exception("invalid amount provided %f" % amount)
        self._amount = amount

    def _set_src_currency(self, src_currency_iso_4217: str):
        if src_currency_iso_4217 not in self.VALID_CURRENCIES:
            raise Exception(
                "invalid source currency ISO code provided %s" % src_currency_iso_4217)
        self._src_currency = src_currency_iso_4217

    def _set_dest_currency(self, dest_currency_iso_4217: str):
        if dest_currency_iso_4217 not in self.VALID_CURRENCIES:
            raise Exception(
                "invalid destination currency ISO code provided %s" % dest_currency_iso_4217)
        self._dest_currency = dest_currency_iso_4217

    def _set_reference_date(self, date_iso_8601: str):
        try:
            reference_date = datetime.strptime(date_iso_8601, "%Y-%m-%d")
        except Exception as e:
            raise Exception(
                "invalid reference date ISO 8601 provided %s" % date_iso_8601)

        if reference_date >= datetime.now():
            raise Exception(
                "reference date could not be in the future %s" % date_iso_8601)

        self._reference_date = reference_date

    @property
    def amount(self) -> float:
        return self._amount

    @property
    def src_currency(self) -> str:
        return self._src_currency

    @property
    def dest_currency(self) -> str:
        return self._dest_currency

    @property
    def reference_date(self) -> datetime:
        return self._reference_date
