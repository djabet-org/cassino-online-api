import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.double_manager import calculate_balance_rolls
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):
    def test_balance(self):
        rolls = [
            {
            "color": "black",
            "created": 1696456720.151,
            "platform": "blaze",
            "roll": 14,
            "total_black_money": 5696.3027,
            "total_red_money": 5223.0806,
            "total_white_money": 16736.426
        },
        {
            "color": "black",
            "created": 1696456690.138,
            "platform": "blaze",
            "roll": 8,
            "total_black_money": 8417.545,
            "total_red_money": 5654.829,
            "total_white_money": 16827.55
        },
        {
            "color": "red",
            "created": 1696456660.122,
            "platform": "blaze",
            "roll": 5,
            "total_black_money": 3920.8267,
            "total_red_money": 10661.167,
            "total_white_money": 17759.555
        },
        {
            "color": "red",
            "created": 1696456630.108,
            "platform": "blaze",
            "roll": 3,
            "total_black_money": 4874.3228,
            "total_red_money": 9121.443,
            "total_white_money": 19756.943
        },
        {
            "color": "red",
            "created": 1696456600.091,
            "platform": "blaze",
            "roll": 6,
            "total_black_money": 5759.6216,
            "total_red_money": 7558.9136,
            "total_white_money": 17846.05
        }
        ]

        result = calculate_balance_rolls(rolls)

        self.assertEqual(result['total'], 4)
        self.assertEqual(result['totalRed'], -1)
        self.assertEqual(result['totalBlack'], 3)
        self.assertEqual(result['totalWhite'], 2)

if __name__ == '__main__':
    unittest.main()