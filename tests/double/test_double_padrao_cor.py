import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.double_manager import probabilidade_padroes_cores
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):
    rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'red' },
            { 'roll': 3, 'color': 'black' },
            { 'roll': 3234, 'color': 'black' },
            { 'roll': 3123, 'color': 'black' },
            { 'roll': 325345, 'color': 'black' },
            { 'roll': 36, 'color': 'black' },
            { 'roll': 423, 'color': 'red' },
            { 'roll': 5, 'color': 'black' },
            { 'roll': 6, 'color': 'red' },
            { 'roll': 7, 'color': 'red' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'red' },
            { 'roll': 8, 'color': 'red' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 9, 'color': 'red' },
            { 'roll': 10, 'color': 'black' },
            { 'roll': 11, 'color': 'red' },
            { 'roll': 12, 'color': 'red' },
        ]

    def test_padrao_cores(self):
        resultAll = probabilidade_padroes_cores(self.rolls, ['b,b,b,b'])['b,b,b,b']
        self.assertEqual(resultAll['black']['probabilidade'], 33)
        self.assertEqual(resultAll['red']['probabilidade'], 66)
        self.assertEqual(resultAll['white']['probabilidade'], 0)

    def test_padrao_cores_galho(self):
        resultAll = probabilidade_padroes_cores(self.rolls, ['b,b,b,b'], 2)['b,b,b,b']
        self.assertEqual(resultAll['black']['probabilidade'], 100)
        self.assertEqual(resultAll['red']['probabilidade'], 100)
        self.assertEqual(resultAll['white']['probabilidade'], 0)

    def test_padrao_cores_targetColor(self):
        resultRed = probabilidade_padroes_cores(self.rolls, ['b,b,b,b'], targetColor='red')['b,b,b,b']
        self.assertEqual(resultRed['red']['probabilidade'], 66)
        self.assertTrue('black' not in resultRed)
        self.assertTrue('white' not in resultRed) 

    def test_padrao_cores_minProbabilidade(self):
        resultAll = probabilidade_padroes_cores(self.rolls, ['b,b,b,b'], minProbabilidade=60)['b,b,b,b']
        self.assertEqual(resultAll['red']['probabilidade'], 66)
        self.assertTrue('black' not in resultAll)
        self.assertTrue('white' not in resultAll)

if __name__ == '__main__':
    unittest.main()