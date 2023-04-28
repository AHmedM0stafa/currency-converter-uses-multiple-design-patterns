[9:40 pm, 28/04/2023] Ahmed Adel: import requests

class CurrencyConverter:
    """A singleton class that provides currency conversion services."""

    _instance = None

    def _new_(cls):
        if cls._instance is None:
            cls.instance = super().new_(cls)
        return cls._instance

    def convert(self, from_currency, to_currency, amount):
        """Converts an amount of money from one currency to another.

        Args:
            from_currency: The currency to convert from.
            to_currency: The currency to convert to.
            amount: The amount of money to convert.

        Returns:
            The converted amount of money.
        """

        # Get the exchange rate from an online source.
        exchange_rate = requests.get("https://api.exchangeratesapi.i…
[10:53 pm, 28/04/2023] sohaila nasr: To fix this error, you need to pass the amount argument when calling the convert method of the CurrencyController instance. For example:
[10:53 pm, 28/04/2023] sohaila nasr: # Create a CurrencyController instance
currency_controller = CurrencyController()

# Convert the amount of money
converted_amount = currency_controller.convert(from_currency, to_currency, amount)
[11:59 pm, 28/04/2023] محمد داله: ahmed adel whare are you?
[0:19 am, 29/04/2023] Ahmed Adel: import requests
import json
import tkinter as tk

from appier.common import model


class CurrencyConverter:
    """A singleton class that provides currency conversion services."""

    _instance = None

    def _new_(cls):
        if cls._instance is None:
            cls.instance = super().new_(cls)
        return cls._instance

    def convert(self, from_currency, to_currency, amount):
        # Get the exchange rate from an online source.
        exchange_rate = requests.get("https://api.exchangeratesapi.io/latest?base={from_currency}").json()["rates"][to_currency]

        # Convert the amount of money.
        converted_amount = amount * exchange_rate

        return converted_amount

class CurrencyFactory:
    """A factory class that creates Currency objects."""

    def _init_(self):
        self._currencies = {}

    def create_currency(self, currency_code):
        """Creates a Currency object for the specified currency code.

        Args:
            currency_code: The currency code.

        Returns:
            The Currency object.
        """

        if currency_code not in self._currencies:
            self._currencies[currency_code] = Currency(currency_code)

        return self._currencies[currency_code]

class Currency:
    """A class that represents a currency."""

    def _init_(self, currency_code):
        self._currency_code = currency_code

    def get_currency_code(self):
        """Returns the currency code."""

        return self._currency_code

    def get_symbol(self):
        """Returns the currency symbol."""

        # TODO: Implement this method.

    def get_exchange_rate(self, to_currency):
        """Returns the exchange rate between this currency and the specified currency.

        Args:
            to_currency: The currency to get the exchange rate for.

        Returns:
            The exchange rate.
        """

        # TODO: Implement this method.
class CurrencyObserver:
    """An abstract class that represents an observer of currency events."""

    def _init_(self):
        pass

    def on_currency_updated(self, currency):
        """Called when a currency is updated.

        Args:
            currency: The currency that was updated.
        """

        pass

class CurrencyState:
    """A class that represents the state of a currency."""

    def _init_(self, currency, exchange_rate):
        self._currency = currency
        self._exchange_rate = exchange_rate

    def get_currency(self):
        """Returns the currency."""

        return self._currency

    def get_exchange_rate(self):
        """Returns the exchange rate."""

        return self._exchange_rate

class CurrencyController:
    """A class that controls the currency converter."""
    def _init_(self):
        self._currency_converter = CurrencyConverter()
        self._currency_factory = CurrencyFactory()
        self._currency_observers = []
        self.from_currency = from_currency
        self.to_currency = to_currency
        self.exchange_rate = 0.0

    def convert(self, from_currency, to_currency, amount):
        url = "https://api.apilayer.com/currency_data/convert?to={to_currency}&from={from_currency}&amount={amount}"

        payload = {}
        headers = {
            "apikey": "aHOW8oAcyjz6TZE6VUAVxJ30owvMtzPW"
        }

        response = requests.request("GET", url, headers=headers, data=payload)


        response = requests.get(url)
        data = response.json()
        self.exchange_rate = data["rates"][self.target_currency]




        return converted_amount

    def add_observer(self, observer):
        """Adds an observer to the currency controller.

        Args:
            observer: The observer to add.
        """

        self._currency_observers.append(observer)

    def remove_observer(self, observer):
        """Removes an observer from the currency controller.

        Args:
            observer: The observer to remove.
        """

        self._currency_observers.remove(observer)

    def _notify_observers(self, currency_state):
        """Notifies the observers of a currency update.

        Args:
            currency_state: The currency state that was updated.
        """

        for observer in self._currency_observers:
            observer.on_currency_updated(currency_state)




class CurrencyConverter:
    def init(self, base_currency, target_currency):
        self.base_currency = base_currency
        self.target_currency = target_currency
        self.exchange_rate = 0.0

    def get_exchange_rate(self):
        url = f"https://api.fixer.io/latest?base={self.base_currency}&symbols={self.target_currency}"
        response = requests.get(url)
        data = response.json()
        self.exchange_rate = data["rates"][self.target_currency]

    def convert_currency(self, amount):
        return amount * self.exchange_rate


class CurrencyConverterFactory:
    @staticmethod
    def create_currency_converter(base_currency, target_currency):
        return CurrencyConverter(base_currency, target_currency)



class CurrencyConverterView:
    def init(self):
        self.amount = float(input("Enter amount: "))
        self.base_currency = input("Enter base currency: ")
        self.target_currency = input("Enter target currency: ")

    def display_converted_amount(self, converted_amount):
        print(f"Converted amount: {converted_amount:.2f}")


class CurrencyConverterController:
    def init(self):
        view = CurrencyConverterView()
        converter = CurrencyConverterFactory.create_currency_converter(view.base_currency, view.target_currency)
        converter.get_exchange_rate()
        converted_amount = converter.convert_currency(view.amount)
        view.display_converted_amount(converted_amount)


if _name_ == "_main_":

    # Get the user input.
    from_currency = input("What currency would you like to convert from? ")
    to_currency = input("What currency would you like to convert to? ")
    amount = int(input("How much money would you like to convert? "))

    currency_controller = CurrencyController()

    # Convert the amount of money.
    converted_amount = currency_controller.convert(from_currency, to_currency, amount)


    # Print the converted amount.
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}.")
