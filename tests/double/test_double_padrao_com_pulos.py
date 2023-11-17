import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.double.double_manager import probabilidade_padroes_cores

class TestManager(unittest.TestCase):
    rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 2, 'color': 'red' },
            { 'roll': 3, 'color': 'red' },
            { 'roll': 3234, 'color': 'black' },
            { 'roll': 3123, 'color': 'black' },
            { 'roll': 325345, 'color': 'black' },
            { 'roll': 36, 'color': 'black' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'red' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'red' },
            { 'roll': 423, 'color': 'red' },
            { 'roll': 423, 'color': 'red' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'black' },
            { 'roll': 423, 'color': 'black' },
        ]

    def test_padrao_com_3_pulos(self):
        resultAll = probabilidade_padroes_cores(self.rolls, ['r,r,r,*,*,*'], galho=2)['r,r,r,*,*,*']
        self.assertEqual(resultAll['black']['probabilidade'], 100)
        self.assertEqual(resultAll['red']['probabilidade'], 50)
        self.assertEqual(resultAll['white']['probabilidade'], 0)

if __name__ == '__main__':
    unittest.main()