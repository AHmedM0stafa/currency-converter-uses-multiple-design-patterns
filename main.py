import argparse
from currency_converter import CurrencyConverter


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--from_currency', type=str, required=True)
    parser.add_argument('--to_currency', type=str, required=True)
    parser.add_argument('--amount', type=float, required=True)

    args = parser.parse_args()

    currency_converter = CurrencyConverter()
    converted_amount = currency_converter.convert(
        from_currency=args.from_currency,
        to_currency=args.to_currency,
        amount=args.amount
    )

    print(f'{args.amount} {args.from_currency} is equal to {converted_amount} {args.to_currency}')


if __name__ == '__main__':
    main()
