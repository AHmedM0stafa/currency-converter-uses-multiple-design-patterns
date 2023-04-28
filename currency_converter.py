import logging

from currency_factory import CurrencyFactory
from currency_rates import CurrencyRates


class CurrencyConverter:
    def __init__(self):
        self.currency_factory = CurrencyFactory()
        self.currency_rates = CurrencyRates()

    def convert(self, from_currency, to_currency, amount):
        from_currency_object = self.currency_factory.create_currency(from_currency)
        to_currency_object = self.currency_factory.create_currency(to_currency)

        exchange_rate = self.currency_rates.get_exchange_rate(from_currency_object, to_currency_object)

        converted_amount = amount * exchange_rate

        return converted_amount
