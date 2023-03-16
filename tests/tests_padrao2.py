import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import src
 
# importing
from src.crash_manager import calculate_padrao2

class TestBlazeCrash(unittest.TestCase):

    def test_padrao2_comeco(self):
        velas = [2,2,5,1,1,1,1,1,1]

        self.assertEqual(calculate_padrao2(velas), 0.5)

    def test_padrao2_meio(self):
        velas = [1,1,1,1,1,2,2,3,1,1,1,1,1,1,1]

        self.assertEqual(calculate_padrao2(velas), 0.5)    

    def test_padrao2_fim(self):
        velas = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,3]

        self.assertEqual(calculate_padrao2(velas), 1)        

    def test_padrao2_80_percentage(self):
        velas = [2, 2, 2, 2, 2, 2, 2, 1]    

        self.assertEqual(calculate_padrao2(velas), 0.8333333333333334)  

if __name__ == '__main__':
    unittest.main()