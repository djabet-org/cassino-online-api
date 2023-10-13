import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import modules

# importing
from modules.crash_manager import probabilidade_padrao_minutos_soma_digitos
from datetime import datetime, timedelta


class TestManager(unittest.TestCase):
    def test_probabilidade_padrao_minutos_soma_digitos_g2(self):
        d = "2023-11-24 09:30:00.000123"
        dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")
        velas = [
            {"created": dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.15,
            },
            {
                "created": (dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 1,
            },
            {
                "created": (dt + timedelta(minutes=10)).timestamp(),
                "platform": "blaze",
                "vela": 1.43,
            },
            {
                "created": (dt + timedelta(minutes=11)).timestamp(),
                "platform": "blaze",
                "vela": 1.14,
            },
            {
                "created": (dt + timedelta(minutes=12)).timestamp(),
                "platform": "blaze",
                "vela": 2,
            },
        ]

        result = probabilidade_padrao_minutos_soma_digitos(velas, 3, 4, 9)
        self.assertEqual(result['assertividade'], "100%")
    def test_probabilidade_padrao_minutos_soma_digitos_sem_galho(self):
        d = "2023-11-24 09:30:00.000123"
        dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")
        velas = [
            {"created": dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.15,
            },
            {
                "created": (dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 1,
            },
            {
                "created": (dt + timedelta(minutes=10)).timestamp(),
                "platform": "blaze",
                "vela": 6,
            },
            {
                "created": (dt + timedelta(minutes=11)).timestamp(),
                "platform": "blaze",
                "vela": 1.14,
            },
            {
                "created": (dt + timedelta(minutes=12)).timestamp(),
                "platform": "blaze",
                "vela": 1,
            },
        ]

        result = probabilidade_padrao_minutos_soma_digitos(velas, 3, 4, 9, 0)
        self.assertEqual(result['assertividade'], "100%")

if __name__ == "__main__":
    unittest.main()
