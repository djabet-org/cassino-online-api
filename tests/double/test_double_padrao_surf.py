import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.double_manager import probabilidade_padrao_surf
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    # def test_padrao_surf_duplo_vermelho(self):
    #     rolls = [
    #         { 'roll': 1, 'color': 'red' },
    #         { 'roll': 1, 'color': 'red' },
    #         { 'roll': 1, 'color': 'black' },
    #         { 'roll': 1, 'color': 'red' },
    #         { 'roll': 1, 'color': 'black' },
    #         { 'roll': 1, 'color': 'red' },
    #         { 'roll': 1, 'color': 'red' },
    #         { 'roll': 1, 'color': 'black' },
    #         { 'roll': 1, 'color': 'red' },
            
    #     ]

    #     result = probabilidade_padrao_surf(rolls, 'red', 2, 2, targetColor='red')
    #     self.assertEqual(result, "100%")

    def test_padrao_surf_duplo_vermelho_black(self):
        rolls = [
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            
        ]

        result = probabilidade_padrao_surf(rolls, 'black', 2, 2, targetColor='black')
        self.assertEqual(result, "50%") 

    def test_padrao_surf_duplo_vermelho_none(self):
        rolls = [
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            
        ]

        result = probabilidade_padrao_surf(rolls, 'black', 2, 2, targetColor='black')
        self.assertEqual(result, "0%")  

    def test_padrao_surf_duplo_vermelho_target_black(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            
        ]

        result = probabilidade_padrao_surf(rolls, 'red', 2, 2, targetColor='black')
        self.assertEqual(result, "100%")

    def test_padrao_surf_duplo_vermelho_target_red(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            
        ]

        result = probabilidade_padrao_surf(rolls, 'black', 2, 2, targetColor='red')
        self.assertEqual(result, "100%")

    def test_padrao_surf_triplo_vermelho_target_red(self):
        rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'red' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 1, 'color': 'red' }
        ]

        result = probabilidade_padrao_surf(rolls, 'black', 2, 2, targetColor='red')
        self.assertEqual(result, "100%")                    

if __name__ == '__main__':
    unittest.main()