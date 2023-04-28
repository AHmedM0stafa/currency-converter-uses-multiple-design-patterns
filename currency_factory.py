import logging

from currency import Currency


class CurrencyFactory:
    def __init__(self):
        self.currencies = {}

    def create_currency(self, currency_code):
        if currency_code not in self.currencies:
            currency = Currency(currency_code)
            self.currencies[currency_code] = currency
        return self.currencies[currency_code]
