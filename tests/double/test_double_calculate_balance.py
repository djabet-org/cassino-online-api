import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import modules

# importing
from modules.double_manager import calculate_balance_rolls
from datetime import datetime, timedelta


class TestManager(unittest.TestCase):
    def test_balance(self):
        rolls = [
            {
                "color": "black",
                "created": 1696568404.515,
                "platform": "blaze",
                "roll": 12,
                "total_black_money": 1546.42,
                "total_red_money": 2927.41,
                "total_white_money": 8545.59,
            },
            {
                "color": "black",
                "created": 1696568374.496,
                "platform": "blaze",
                "roll": 10,
                "total_black_money": 23513.3,
                "total_red_money": 2863.34,
                "total_white_money": 13154.43,
            },
            {
                "color": "black",
                "created": 1696568344.475,
                "platform": "blaze",
                "roll": 8,
                "total_black_money": 1603.37,
                "total_red_money": 1169.78,
                "total_white_money": 9393.54,
            },
            {
                "color": "red",
                "created": 1696568314.456,
                "platform": "blaze",
                "roll": 6,
                "total_black_money": 3278.78,
                "total_red_money": 1019.1,
                "total_white_money": 8836.57,
            },
            {
                "color": "black",
                "created": 1696568284.436,
                "platform": "blaze",
                "roll": 8,
                "total_black_money": 1582.25,
                "total_red_money": 4319.86,
                "total_white_money": 9154.26,
            },
            {
                "color": "red",
                "created": 1696568254.416,
                "platform": "blaze",
                "roll": 6,
                "total_black_money": 1721.2,
                "total_red_money": 7435.11,
                "total_white_money": 8988.36,
            },
        ]

        result = calculate_balance_rolls(rolls)

        self.assertEqual(round(result["black"], 2), -23245.36)
        self.assertEqual(round(result["red"], 2), 2826.18)
        self.assertEqual(round(result["white"], 2), 58072.75)
        self.assertEqual(round(result["total"], 2), 37653.57)


if __name__ == "__main__":
    unittest.main()
