import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import modules

# importing
from modules.double_manager import probabilidade_padrao_minutos_intervalos
from datetime import datetime, timedelta


class TestManager(unittest.TestCase):
    d = "2023-11-24 09:30:00.000123"
    dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")

    def test_probabilidade_padrao_minutos_intervalos_black_sem_galho(self):
        velas = [
            {
                "color": "black",
                "created": (self.dt + timedelta(minutes=3)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 0, desiredColor="black")
        self.assertEqual(result[3]['probabilidade'], "100%")

    def test_probabilidade_padrao_minutos_intervalos_black_g1(self):
        velas = [
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=3)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "black",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 1, desiredColor="black")
        self.assertEqual(result[3]['probabilidade'], "100%")

    def test_probabilidade_padrao_minutos_intervalos_black_g2(self):
        velas = [
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=3)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "black",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 2, desiredColor="black")
        self.assertEqual(result[3]['probabilidade'], "100%")

    def test_probabilidade_padrao_minutos_intervalos_black_not_found(self):
        velas = [
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=3)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
            {
                "color": "red",
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "roll": 9,
                "total_black_money": 1752.78,
                "total_red_money": 7144.55,
                "total_white_money": 9285.43,
            },
        ]

        result = probabilidade_padrao_minutos_intervalos(velas, 2, desiredColor="black")
        self.assertEqual(result[3]['probabilidade'], "0%")


if __name__ == "__main__":
    unittest.main()
