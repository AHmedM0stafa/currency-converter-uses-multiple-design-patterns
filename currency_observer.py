import logging

from currency import Currency


class CurrencyObserver:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, currency):
        for observer in self.observers:
            observer.update(currency)
            
# import logging

# from currency import Currency


# class CurrencyObserver:
#     def __init__(self):
#         self.observers = []

#     def add_observer(self, observer):
#         self.observers.append(observer)

#     def notify_observers(self, currency):
#         for observer in self.observers:
#             observer.update(currency)


# class CurrencyPriceObserver:
#     def __init__(self, currency):
#         self.currency = currency

#     def update(self, currency):
#         print("The price of {} has changed".format(self.currency))


# if __name__ == "__main__":
#     currency_observer = CurrencyObserver()
#     currency_price_observer = CurrencyPriceObserver("USD")
#     currency_observer.add_observer(currency_price_observer)

#     currency_observer.notify_observers(Currency("USD"))
