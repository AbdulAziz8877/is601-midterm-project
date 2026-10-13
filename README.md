# Dosa Restaurant Order Processing

## Description

This project processes JSON orders from a dosa restaurant. It creates two JSON files containing customer information and menu item statistics.

## Output Files

- `customers.json`: Stores customer phone numbers as keys and customer names as values.
- `items.json`: Stores menu item names, prices, and the number of times each item was ordered.

## Requirements

- Python 3
- No external libraries required.

## How to Run

Open a terminal in the `midterm_project` directory and run:

```bash
python main.py example_orders.json
```

The program creates `customers.json` and `items.json` in the current directory.

You can also provide another JSON file as the first command-line argument.

## How It Works

The program uses `argparse` to read the input filename. It loads the orders from the JSON file, collects customer information, counts the occurrences of menu items, and writes the results to two output JSON files.