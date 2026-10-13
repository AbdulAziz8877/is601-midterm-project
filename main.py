
import argparse
import json


def is_valid_phone(phone):
    """Check whether a phone number uses xxx-xxx-xxxx format."""
    return (
        isinstance(phone, str)
        and len(phone) == 12
        and phone[3] == "-"
        and phone[7] == "-"
        and phone.replace("-", "").isdigit()
    )


def process_orders(orders):
    """Collect customer details and count menu item orders."""
    customers = {}
    items = {}

    if not isinstance(orders, list):
        raise ValueError("Input JSON must contain a list of orders.")

    for order in orders:
        if not isinstance(order, dict):
            continue

        if "phone" in order and "name" in order:
            phone = order["phone"]

            if is_valid_phone(phone):
                customers[phone] = order["name"]

        order_items = order.get("items", [])

        if not isinstance(order_items, list):
            continue

        for item in order_items:
            if not isinstance(item, dict):
                continue

            if "name" not in item or "price" not in item:
                continue

            item_name = item["name"]

            if item_name not in items:
                items[item_name] = {
                    "price": item["price"],
                    "orders": 0
                }

            items[item_name]["orders"] += 1

    return customers, items


def save_json(filename, data):
    """Save data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Process dosa restaurant orders"
    )
    parser.add_argument("filename", help="Input JSON file")
    args = parser.parse_args()

    try:
        with open(args.filename, "r", encoding="utf-8") as file:
            orders = json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{args.filename}' was not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: File '{args.filename}' is not valid JSON.")
        return

    try:
        customers, items = process_orders(orders)
    except ValueError as error:
        print(f"Error: {error}")
        return

    try:
        save_json("customers.json", customers)
        save_json("items.json", items)
    except OSError as error:
        print(f"Error saving output files: {error}")
        return

    print("Successfully created customers.json and items.json.")


if __name__ == "__main__":
    main()
