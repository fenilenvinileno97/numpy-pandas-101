#!/usr/bin/env python3
import unittest
from char_detection import char_type

class TestEncode(unittest.TestCase):
    
    def test_utf8(self):
        testcase = "../../Datasets/Threatened_species.csv"
        expected = "utf-8"
        self.assertEqual(char_type(testcase), expected)
        
    def test_cp(self):
        testcase = "../../Datasets/CO2_emission_by_countries.csv"
        expected = "CP949"
        self.assertEqual(char_type(testcase), expected)

if __name__ == '__main__':
    unittest.main(verbosity=True)