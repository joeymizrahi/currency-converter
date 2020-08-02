

import unittest
import os
import sys
import requests


class TestConverter(unittest.TestCase):

    def setUp(self):
        self.converter = Converter.Converter()
        return super().setUp()

    def test_bad_currency(self):
        with self.assertRaises(ValueError):
            res = self.converter.convert("USD", "NIS", 3)

    def test_bad_ammount(self):
        with self.assertRaises(ValueError):
            res = self.converter.convert("USD", "ILS", "3")

    def test_conversion_diff_currencies(self):
        # TODO, find a way to check the functionality
        pass


if __name__ == '__main__':
    sys.path.insert(0, os.path.join(sys.path[0], os.pardir))
    import Converter
    unittest.main()
