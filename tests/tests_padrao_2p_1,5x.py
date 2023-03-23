import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import calculate_padrao_2p_15x_g2

class TestBlazeCrash(unittest.TestCase):

    def test1_calculate_padrao_2p_15x_g2(self):
        velas = [2, 3, 4, 5, 6, 7, 8, 1.25, 1.24, 2]

        self.assertEqual(calculate_padrao_2p_15x_g2(velas), 1)

    def test2_calculate_padrao_2p_14x_g2(self):
        velas = [2, 3, 4, 5, 6, 7, 8, 1.25, 1.24, 1, 2]

        self.assertEqual(calculate_padrao_2p_15x_g2(velas), 1)

    def test3_calculate_padrao_2p_14x_g2(self):
        velas = [2, 3, 4, 5, 6, 7, 8, 1.25, 1.24, 1, 1, 2]

        self.assertEqual(calculate_padrao_2p_15x_g2(velas), 1)

    def test4_calculate_padrao_2p_13x_g2(self):
        velas = [2, 3, 4, 5, 6, 7, 8, 1.25, 1.24, 1, 1, 1]

        self.assertEqual(calculate_padrao_2p_15x_g2(velas), 0)

    def test5_calculate_padrao_2p_14x_g2(self):
        velas = [1.25, 1.24, 4, 5, 6, 7, 8, 1.25, 1.24, 1.55, 1.55, 1.55]

        self.assertEqual(calculate_padrao_2p_15x_g2(velas), 0.5)        

if __name__ == '__main__':
    unittest.main()