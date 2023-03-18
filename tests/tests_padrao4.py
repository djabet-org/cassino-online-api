import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '..')))

import modules
 
# importing
from modules.crash_manager import calculate_padrao4_g2

class TestBlazeCrash(unittest.TestCase):

    def test_padrao4_1(self):
        velas = [1.6,1.6,1.6,1.6,1.4,1.3,2,1]

        self.assertEqual(calculate_padrao4_g2(velas), 1)

    def test_padrao4_2(self):
        velas = [1.6,1.6,1.6,1.6,1.4,1.3,1.6,2]

        self.assertEqual(calculate_padrao4_g2(velas), 1)   

    def test_padrao4_3(self):
        velas = [3,3,3,3,3,3,3,1,1,1.7,1.7,2]

        self.assertEqual(calculate_padrao4_g2(velas), 1)           

if __name__ == '__main__':
    unittest.main()