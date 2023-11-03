import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import modules

# importing
from modules.crash.crash_manager import probabilidade_padrao_intervalos_para_velaX
from datetime import datetime, timedelta


class TestManager(unittest.TestCase):

    d = "2023-11-24 09:30:00.000123"
    dt = datetime.strptime(d, "%Y-%m-%d %H:%M:%S.%f")

    @classmethod
    def setUpClass(self):
        self.search_filter = {
            'qtd_galho': 0,
            'target_vela': 2,
            'min_probabilidade': 0,
        }

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

        self.search_filter['velas'] = velas

        result = probabilidade_padrao_intervalos_para_velaX([3, 4], afterQtdMinutes=0, search_filters=self.search_filter)
        self.assertEqual(result['probabilidade'], 100)
    
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

        self.search_filter['velas'] = velas
        result = probabilidade_padrao_intervalos_para_velaX([3, 4], 0, self.search_filter)
        self.assertEqual(result['probabilidade'], 0)
    
    def test_probabilidade_padrao_minutos_intervalos_para_vela_afterQtdMinutos(self):
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

        self.search_filter['velas'] = velas

        result = probabilidade_padrao_intervalos_para_velaX([3, 4], 7, self.search_filter)
        self.assertEqual(result['probabilidade'], 100)
    
    def test_probabilidade_padrao_minutos_intervalos_para_vela_afterQtdMinutos_nao_achou(self):
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

        self.search_filter['velas'] = velas

        result = probabilidade_padrao_intervalos_para_velaX([3, 4], 7, self.search_filter)
        self.assertEqual(result['probabilidade'], 0)
    
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
                "vela": 1.3,
            },
            {
                "created": (self.dt + timedelta(minutes=9)).timestamp(),
                "platform": "blaze",
                "vela": 2.1,
            }
        ]

        self.search_filter['velas'] = velas
        self.search_filter['qtd_galho'] = 2

        result = probabilidade_padrao_intervalos_para_velaX([3, 4], 0, self.search_filter)
        self.assertEqual(result['probabilidade'], 100)
    
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

        self.search_filter['velas'] = velas
        self.search_filter['qtd_galho'] = 2

        result = probabilidade_padrao_intervalos_para_velaX([3, 4], 0, self.search_filter)
        self.assertEqual(result['probabilidade'], 0)
    
    def test_probabilidade_padrao_minutos_intervalos_para_vela_targetVela(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3,
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

        self.search_filter['velas'] = velas
        self.search_filter['target_vela'] = 4
        self.search_filter['qtd_galho'] = 2

        result = probabilidade_padrao_intervalos_para_velaX([3,4], 0, self.search_filter)
        self.assertEqual(result['probabilidade'], 100)
    
    def test_probabilidade_padrao_minutos_intervalos_para_vela_targetVela_nao_achou(self):
        velas = [
            {"created": self.dt.timestamp(), "platform": "blaze", "vela": 1.16},
            {
                "created": (self.dt + timedelta(minutes=1)).timestamp(),
                "platform": "blaze",
                "vela": 3,
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

        self.search_filter['velas'] = velas
        self.search_filter['qtd_galho'] = 2
        self.search_filter['target_vela'] = 4

        result = probabilidade_padrao_intervalos_para_velaX([3, 4], 0, self.search_filter)
        self.assertEqual(result['probabilidade'], 0)

if __name__ == "__main__":
    unittest.main()
