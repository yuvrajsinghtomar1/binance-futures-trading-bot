import argparse

from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price"
    )

    args = parser.parse_args()

    try:

        symbol = args.symbol.upper()

        side = validate_side(args.side)

        order_type = validate_order_type(args.type)

        quantity = validate_quantity(args.quantity)

        price = None

        if order_type == "LIMIT":
            price = validate_price(args.price)

        print("\n===== ORDER REQUEST =====")

        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        response = place_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        print("\n===== ORDER RESPONSE =====")

        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(
            f"Average Price: "
            f"{response.get('avgPrice', 'N/A')}"
        )

        print("\nOrder placed successfully!")

    except Exception as e:

        print(f"\nOrder failed: {e}")


if __name__ == "__main__":
    main()