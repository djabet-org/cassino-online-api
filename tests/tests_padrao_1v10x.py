import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import calculate_padrao_1v10x_g2

class TestBlazeCrash(unittest.TestCase):

    def test1_calculate_padrao_1v10x_g2(self):
        velas = [1,2,5,1,1,1,1,10,2]

        self.assertEqual(calculate_padrao_1v10x_g2(velas), 1)

    def test2_calculate_padrao_1v10x_g2(self):
        velas = [1,1,1,1,1,2,2,3,1,1,1,1,10,1,2]

        self.assertEqual(calculate_padrao_1v10x_g2(velas), 1)    

    def test3_calculate_padrao_1v10x_g2(self):
        velas = [1,1,1,1,1,1,1,1,1,1,1,1,1,10,2,3,3]

        self.assertEqual(calculate_padrao_1v10x_g2(velas), 1)        

    def test4_calculate_padrao_1v10x_g2(self):
        velas = [10, 2, 1, 2, 12, 1, 1]    

        self.assertEqual(calculate_padrao_1v10x_g2(velas), 0.5)

    def test5_calculate_padrao_1v10x_g2(self):
        velas = [1, 2, 1, 2, 1, 1, 1]    

        self.assertEqual(calculate_padrao_1v10x_g2(velas), 0)      

if __name__ == '__main__':
    unittest.main()