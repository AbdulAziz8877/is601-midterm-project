# 🥞 Dosa Restaurant Order Processor

A simple Python project that organizes restaurant order data from a JSON file. It collects customer details, tracks popular menu items, and creates separate JSON files for the results.

## 📌 Project Overview

Restaurants receive orders containing customer information and the items they purchase. This program processes that information automatically instead of requiring someone to organize it manually.

The program takes an input JSON file and generates two output files: one for customer information and another for menu item statistics.

## ✨ Features

- **Customer Records:** Stores customer names using their phone numbers as keys.
- **Phone Number Validation:** Includes only phone numbers that match the `xxx-xxx-xxxx` format.
- **Menu Item Tracking:** Counts how many times each menu item appears in the orders.
- **Price Information:** Stores the price of each menu item.
- **Input Error Handling:** Displays a helpful message if the input file is missing or contains invalid JSON.
- **Automatic Output:** Creates the output files without requiring manual data entry.

## 📂 Project Structure

```text
midterm_project/
├── main.py
├── example_orders.json
├── customers.json
├── items.json
└── README.md
```

- `main.py` — Main Python program.
- `example_orders.json` — Sample restaurant order data.
- `customers.json` — Generated customer records.
- `items.json` — Generated menu item statistics.
- `README.md` — Project documentation.

*Note: The two output files are generated when the program runs.*

## ⚙️ Requirements

- Python 3
- Python standard libraries: `argparse` and `json`

No additional packages are required.

## ▶️ How to Run

**Step 1:** Open a terminal in the project directory.

**Step 2:** Run the program with the input filename:

```bash
python main.py example_orders.json
```

**Step 3:** Check the directory for the generated `customers.json` and `items.json` files.

You can also provide another JSON file as the command-line argument.

## 📄 Output Details

### 1. `customers.json`

Contains phone numbers as keys and customer names as values.

Example:

```json
{
    "732-555-5509": "Damodhar"
}
```

### 2. `items.json`

Contains each menu item's name, price, and order count.

Example:

```json
{
    "Cheese Madurai Masala Dosa": {
        "price": 13.95,
        "orders": 1
    }
}
```

The example above illustrates the output structure; actual counts depend on the input data.

## 🛡️ Error Handling

The program handles common input problems:

- If the input file does not exist, it displays a file-not-found message.
- If the input file contains invalid JSON, it displays an invalid-JSON message.

For example:

```bash
python main.py missing.json
```

The program displays an error message instead of showing a Python traceback.

## 🧠 What I Learned

Through this project, I practiced reading JSON data in Python, working with dictionaries, using loops and conditional statements, accepting command-line arguments, validating phone numbers, handling input errors, and writing JSON output files.

## 👨‍💻 Project Information

**Course:** IS601

**Project:** Midterm Project — Python Order Processing

**Language:** Python

## 🎯 Conclusion

This project demonstrates how Python can be used to process structured restaurant data and turn it into useful customer records and menu statistics. It also provides practice with file handling, data organization, and basic error handling.

## 🧪 Automated Testing

This project includes automated tests using Python's built-in `unittest` module. These tests help check that the main functions work correctly.

The tests cover:

- Valid and invalid phone numbers
- Customer information processing
- Menu item order counts
- Invalid top-level input data

### Run the Tests

Open a terminal in the project directory and run:

```bash
python -m unittest -v
```

The test results show whether each test passes or fails. If all tests pass, the output ends with `OK`.

No additional testing packages are required.