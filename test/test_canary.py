import unittest
# from math import add
# from lib import add
from lib.math import add

class TestCanary(unittest.TestCase):

    def test_upper(self):
        self.assertEqual("foo".upper(), "FOO")

    def test_add(self):
        self.assertEqual(add(5, 2), 7)
