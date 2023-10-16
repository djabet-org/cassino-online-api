import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import modules

# importing
from modules.crash_manager import probabilidade_padrao_intervalos_para_velaX
from datetime import datetime, timedelta


class TestManager(unittest.TestCase):

    d = "2023-11-24 09:30:00.000123"
    dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")
     
    def test_probabilidade_padrao_minutos_intervalos_para_vela(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.3,
            },
            {
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "vela": 2,
            },
            {
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "vela": 1,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, 3, 4, 0, 0)
        self.assertEqual(result['assertividade'], "100%")
    def test_probabilidade_padrao_minutos_intervalos_para_vela_nao_achou(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.3,
            },
            {
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "vela": 1.1,
            },
            {
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, 3, 4, 0, 0)
        self.assertEqual(result['assertividade'], "0%")
    def test_probabilidade_padrao_minutos_intervalos_para_vela_minutos(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.3,
            },
            {
                "created": (self.dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 1.1,
            },
            {
                "created": (self.dt + timedelta(minutes=8)).timestamp(),
                "platform": "blaze",
                "vela": 2,
            },
            {
                "created": (self.dt + timedelta(minutes=9)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, 3, 4, 7, 0)
        self.assertEqual(result['assertividade'], "100%")
    def test_probabilidade_padrao_minutos_intervalos_para_vela_minutos_nao_achou(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.3,
            },
            {
                "created": (self.dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 3.2,
            },
            {
                "created": (self.dt + timedelta(minutes=8)).timestamp(),
                "platform": "blaze",
                "vela": 1.1,
            },
            {
                "created": (self.dt + timedelta(minutes=9)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, 3, 4, 7, 0)
        self.assertEqual(result['assertividade'], "0%")
    def test_probabilidade_padrao_minutos_intervalos_para_vela_g2(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.3,
            },
            {
                "created": (self.dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            },
            {
                "created": (self.dt + timedelta(minutes=8)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            },
            {
                "created": (self.dt + timedelta(minutes=9)).timestamp(),
                "platform": "blaze",
                "vela": 2.1,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, 3, 4, 0, 2)
        self.assertEqual(result['assertividade'], "100%")
    def test_probabilidade_padrao_minutos_intervalos_para_vela_g2_nao_achou(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3.3,
            },
            {
                "created": (self.dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            },
            {
                "created": (self.dt + timedelta(minutes=8)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            },
            {
                "created": (self.dt + timedelta(minutes=9)).timestamp(),
                "platform": "blaze",
                "vela": 1.3,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, 3, 4, 0, 2)
        self.assertEqual(result['assertividade'], "0%")
    def test_probabilidade_padrao_minutos_intervalos_para_vela_targetVela(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 2.7,
            },
            {
                "created": (self.dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 1.1,
            },
            {
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            },
            {
                "created": (self.dt + timedelta(minutes=5)).timestamp(),
                "platform": "blaze",
                "vela": 6,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, targetVela=4)
        self.assertEqual(result['assertividade'], "100%")
    def test_probabilidade_padrao_minutos_intervalos_para_vela_targetVela_nao_achou(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 2.7,
            },
            {
                "created": (self.dt + timedelta(minutes=2)).timestamp(),
                "platform": "blaze",
                "vela": 1.1,
            },
            {
                "created": (self.dt + timedelta(minutes=4)).timestamp(),
                "platform": "blaze",
                "vela": 1.2,
            },
            {
                "created": (self.dt + timedelta(minutes=5)).timestamp(),
                "platform": "blaze",
                "vela": 3.9,
            }
        ]

        result = probabilidade_padrao_intervalos_para_velaX(velas, targetVela=4)
        self.assertEqual(result['assertividade'], "0%")

if __name__ == "__main__":
    unittest.main()
