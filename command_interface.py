import argparse
from currency_converter import CurrencyConverter


class CommandInterface:
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('--from_currency', type=str, required=True)
        self.parser.add_argument('--to_currency', type=str, required=True)
        self.parser.add_argument('--amount', type=float, required=True)

    def run(self):
        args = self.parser.parse_args()

        currency_converter = CurrencyConverter()
        converted_amount = currency_converter.convert(
            from_currency=args.from_currency,
            to_currency=args.to_currency,
            amount=args.amount
        )

        print(f'{args.amount} {args.from_currency} is equal to {converted_amount} {args.to_currency}')


if __name__ == '__main__':
    command_interface = CommandInterface()
    command_interface.run()
