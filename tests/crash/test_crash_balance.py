import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import modules

# importing
from modules.crash_manager import calculate_balance
from datetime import datetime, timedelta


class TestManager(unittest.TestCase):
    def test_calculate_balance(self):
        velas = [
            {
                "created": 1696525913.433,
                "platform": "blaze",
                "total_bets_placed": 478,
                "total_money_bets": 2992.0,
                "total_money_bets_won": 1040.5,
                "vela": 2.24,
            },
            {
                "created": 1696525889.967,
                "platform": "blaze",
                "total_bets_placed": 597,
                "total_money_bets": 3779.47,
                "total_money_bets_won": 0.0,
                "vela": 1.18,
            },
            {
                "created": 1696525877.184,
                "platform": "blaze",
                "total_bets_placed": 662,
                "total_money_bets": 3040.0,
                "total_money_bets_won": 1727.4,
                "vela": 3.07,
            },
            {
                "created": 1696525848.462,
                "platform": "blaze",
                "total_bets_placed": 662,
                "total_money_bets": 3668.0,
                "total_money_bets_won": 5298.44,
                "vela": 4.86,
            },
            {
                "created": 1696525812.085,
                "platform": "blaze",
                "total_bets_placed": 708,
                "total_money_bets": 3148.0,
                "total_money_bets_won": 750.9,
                "vela": 2.58,
            },
        ]
        result = calculate_balance(velas)
        self.assertEqual(result, 7810.23)

if __name__ == "__main__":
    unittest.main()
