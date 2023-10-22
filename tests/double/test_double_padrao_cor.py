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
    def test_padrao_cores(self):
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
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 8, 'color': 'black' },
            { 'roll': 9, 'color': 'red' },
            { 'roll': 10, 'color': 'black' },
            { 'roll': 11, 'color': 'red' },
            { 'roll': 12, 'color': 'red' },
            
        ]

        resultRed = probabilidade_padroes_cores(rolls, ['b,b,b,b'], 2, 50, 'red')['b,b,b,b']
        resultBlack = probabilidade_padroes_cores(rolls, ['b,b,b,b'], 2, 50, 'black')['b,b,b,b']
        resultAll = probabilidade_padroes_cores(rolls, ['b,b,b,b'], 2, 50)['b,b,b,b']

        self.assertEqual(resultRed['red']['probabilidade'], 50)
        self.assertTrue('black' not in resultRed)
        self.assertTrue('white' not in resultRed)
        self.assertEqual(resultBlack['black']['probabilidade'], 100)
        self.assertTrue('red' not in resultBlack)
        self.assertTrue('white' not in resultBlack)
        self.assertEqual(resultAll['black']['probabilidade'], 100)
        self.assertEqual(resultAll['red']['probabilidade'], 50)
        self.assertEqual(resultAll['white'], {})

if __name__ == '__main__':
    unittest.main()