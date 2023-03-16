import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import src
 
# importing
from src.crash_manager import calculate_padrao3

class TestBlazeCrash(unittest.TestCase):

    def test_padrao3_comeco(self):
        velas = [10,2,5,1,1,1,1,1,1]

        self.assertEqual(calculate_padrao3(velas), 1)

    def test_padrao3_meio(self):
        velas = [1,1,1,1,1,2,20,3,1,1,1,1,1,1,1]

        self.assertEqual(calculate_padrao3(velas), 1)    

    def test_padrao3_fim(self):
        velas = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,23,3]

        self.assertEqual(calculate_padrao3(velas), 1)        

    def test_padrao2_50_percentage(self):
        velas = [10, 12, 1, 2, 2, 2, 1]    

        self.assertEqual(calculate_padrao3(velas), 0.5)  

if __name__ == '__main__':
    unittest.main()