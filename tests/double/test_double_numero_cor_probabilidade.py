import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.double_manager import calculate_roll_next_color_probability
from datetime import datetime, timedelta

class TestManager(unittest.TestCase):

    rolls = [
            { 'roll': 1, 'color': 'red' },
            { 'roll': 0, 'color': 'red' },
            { 'roll': 3, 'color': 'red' },
            { 'roll': 4, 'color': 'black' },
            { 'roll': 5, 'color': 'black' },
            { 'roll': 1, 'color': 'black' },
            { 'roll': 0, 'color': 'black' },
            { 'roll': 3, 'color': 'black' },
            { 'roll': 10, 'color': 'black' },
            { 'roll': 5, 'color': 'red' },
            { 'roll': 0, 'color': 'white' },
            { 'roll': 5, 'color': 'white' },
        ]

    def test_numero_cor_probabilidade(self):
        result = calculate_roll_next_color_probability(self.rolls)
        self.assertEqual(result[0]["red"]['hit'], 1)
        self.assertEqual(result[0]["red"]['tried'], 3)
        self.assertEqual(result[0]["red"]['probabilidade'], 33)

    def test_numero_cor_probabilidade_targetColor(self):
        result = calculate_roll_next_color_probability(self.rolls, targetColor='red')
        self.assertEqual(result[0]["red"]['hit'], 1)
        self.assertEqual(result[0]["red"]['tried'], 3)
        self.assertEqual(result[0]["red"]['probabilidade'], 33)    
        self.assertFalse('black' in result[0])    
        self.assertFalse('white' in result[0])    

    def test_numero_cor_probabilidade_targetColor_allColors(self):
        result = calculate_roll_next_color_probability(self.rolls, targetColor='*')
        self.assertTrue('black' in result[0])        
        self.assertTrue('red' in result[0])        
        self.assertTrue('white' in result[0])        

    def test_numero_cor_probabilidade_galho(self):
        result = calculate_roll_next_color_probability(self.rolls, galho=2)
        self.assertEqual(result[0]["red"]['hit'], 2)
        self.assertEqual(result[0]["red"]['tried'], 3)
        self.assertEqual(result[0]["red"]['probabilidade'], 66)

    def test_numero_cor_probabilidade_minProbabilidade(self):
        result = calculate_roll_next_color_probability(self.rolls, minProbabilidade=60)
        self.assertTrue(0 not in result)        
        self.assertTrue(10 in result)        
        self.assertTrue('red' in result[10])        
        self.assertTrue('white' not in result[10])        
        self.assertTrue('black' not in result[10])        

if __name__ == '__main__':
    unittest.main()