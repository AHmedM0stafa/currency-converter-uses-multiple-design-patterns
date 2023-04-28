import logging

from currency import Currency


class CurrencyRates:
    def __init__(self):
        self.rates = {}

    def get_exchange_rate(self, from_currency, to_currency):
        if from_currency not in self.rates or to_currency not in self.rates:
            logging.warning(f'Exchange rate for {from_currency} to {to_currency} is not available.')
            return None
        return self.rates[from_currency][to_currency]

    def update_rates(self, rates):
        self.rates = rates
