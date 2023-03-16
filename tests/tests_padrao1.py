import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import src
 
# importing
from src.crash_manager import calculate_padrao1

class TestBlazeCrash(unittest.TestCase):

    def test_padrao1_comeco(self):
        velas = [2,2,2,3,1,1,1,1,1,1,1]

        self.assertEqual(calculate_padrao1(velas), 0.5)

    def test_padrao1_meio(self):
        velas = [1,1,1,1,1,2,2,2,3,1,1,1,1,1,1,1]

        self.assertEqual(calculate_padrao1(velas), 0.5)    

    def test_padrao1_fim(self):
        velas = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3]

        self.assertEqual(calculate_padrao1(velas), 1)        

    def test_padrao1_50_percentage(self):
        velas = [1,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,3]    

        self.assertEqual(calculate_padrao1(velas), 0.5)  

    def test_padrao1_80_percentage(self):
        velas = [2, 2, 2, 2, 2, 2, 2, 1]    

        self.assertEqual(calculate_padrao1(velas), 0.8)  

if __name__ == '__main__':
    unittest.main()