
import unittest

from main import is_valid_phone, process_orders


class TestOrderProcessor(unittest.TestCase):

    def test_valid_phone(self):
        self.assertTrue(is_valid_phone("732-555-5509"))

    def test_invalid_phone(self):
        self.assertFalse(is_valid_phone("7325555509"))
        self.assertFalse(is_valid_phone("abc-def-ghij"))

    def test_customer_processing(self):
        orders = [
            {
                "name": "Damodhar",
                "phone": "732-555-5509",
                "items": []
            }
        ]

        customers, items = process_orders(orders)

        self.assertEqual(
            customers,
            {"732-555-5509": "Damodhar"}
        )
        self.assertEqual(items, {})

    def test_item_count(self):
        orders = [
            {
                "name": "Damodhar",
                "phone": "732-555-5509",
                "items": [
                    {"name": "Masala Dosa", "price": 13.95},
                    {"name": "Masala Dosa", "price": 13.95}
                ]
            }
        ]

        customers, items = process_orders(orders)

        self.assertEqual(items["Masala Dosa"]["orders"], 2)
        self.assertEqual(items["Masala Dosa"]["price"], 13.95)

    def test_invalid_top_level_data(self):
        with self.assertRaises(ValueError):
            process_orders({"name": "Damodhar"})


if __name__ == "__main__":
    unittest.main()
