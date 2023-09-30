import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import probabilidade_padrao_xadrez

class TestManager(unittest.TestCase):

    # def test_probabilidade_xadrez_simples(self):
    #     velas = [
    #         { 'vela': 2.4 },
    #         { 'vela': 1 },
    #         { 'vela': 2 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 2 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 1 },
    #         { 'vela': 2 }
    #     ]

    #     result = probabilidade_padrao_xadrez(velas, 1, 2)
    #     self.assertEqual(result, '100%')

    # def test_probabilidade_xadrez_simples_2(self):
    #     velas = [
    #         { 'vela': 2.4 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 2 }
    #     ]

    #     result = probabilidade_padrao_xadrez(velas, 1, 2)
    #     self.assertEqual(result, '0%') 

    # def test_probabilidade_xadrez_simples_3(self):
    #     velas = [
    #         { 'vela': 2.4 },
    #         { 'vela': 1 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 2 },
    #         { 'vela': 1 },
    #         { 'vela': 0 },
    #         { 'vela': 0 },
    #         { 'vela': 0 },
    #     ]

    #     result = probabilidade_padrao_xadrez(velas, 1, 2)
    #     self.assertEqual(result, '50%')

    def test_probabilidade_xadrez_duplo(self):
        velas = [
                { 'vela': 2.4 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 2 },
                { 'vela': 2 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 2 }
        ]

        result = probabilidade_padrao_xadrez(velas, 2, 2)
        self.assertEqual(result, '100%') 

    def test_probabilidade_xadrez_duplo_2(self):
        velas = [
                { 'vela': 2.4 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 2 }
        ]

        result = probabilidade_padrao_xadrez(velas, 2, 2)
        self.assertEqual(result, '50%') 

    def test_probabilidade_xadrez_duplo_3(self):
        velas = [
                { 'vela': 2.4 },
                { 'vela': 2 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 2 },
                { 'vela': 2 },
                { 'vela': 2 },
                { 'vela': 1 },
                { 'vela': 1 },
                { 'vela': 2 }
        ]

        result = probabilidade_padrao_xadrez(velas, 2, 2)
        self.assertEqual(result, '0%')                    

if __name__ == '__main__':
    unittest.main()