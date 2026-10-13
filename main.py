import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        description="Process dosa restaurant orders"
    )
    parser.add_argument("filename", help="Input JSON file")
    args = parser.parse_args()

    with open(args.filename, "r", encoding="utf-8") as file:
        orders = json.load(file)

    customers = {}
    items = {}

    for order in orders:
        phone = order["phone"]

        if (
            isinstance(phone, str)
            and len(phone) == 12
            and phone[3] == "-"
            and phone[7] == "-"
            and phone.replace("-", "").isdigit()
        ):
            customers[phone] = order["name"]

        for item in order["items"]:
            item_name = item["name"]

            if item_name not in items:
                items[item_name] = {
                    "price": item["price"],
                    "orders": 0
                }

            items[item_name]["orders"] += 1

    with open("customers.json", "w", encoding="utf-8") as file:
        json.dump(customers, file, indent=4)

    with open("items.json", "w", encoding="utf-8") as file:
        json.dump(items, file, indent=4)

    print("Successfully created customers.json and items.json.")


if __name__ == "__main__":
    main()