import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_padrao_xadrez

class TestManager(unittest.TestCase):

    def test_probabilidade_xadrez_duplo_g2_targetVela_4(self):
        velas = [
            { 'vela': 2.4 },
            { 'vela': 1 },
            { 'vela': 2 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 4.3},
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 1 },
            { 'vela': 2 }
        ]

        result = probabilidade_padrao_xadrez(velas, 2, 2, 50)
        self.assertEqual(result[2]['probabilidade'], 100)

    def test_probabilidade_xadrez_triplo_g2_targetVela_4(self):
        velas = [
            { 'vela': 2.4 },
            { 'vela': 1 },
            { 'vela': 5 },
            { 'vela': 1 },
            { 'vela': 1234 },
            { 'vela': 1 },
            { 'vela': 4.3},
        ]

        result = probabilidade_padrao_xadrez(velas, 2, 10, 0)
        self.assertEqual(result[3]['probabilidade'], 0)

if __name__ == '__main__':
    unittest.main()