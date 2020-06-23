import unittest
from sample import *

class TestCase(unittest.TestCase):
    def setUp(self)-> None:
        self.cal = Math()

    def tearDown(self)-> None:
        pass

    def test_add(self):
        res = self.cal.add(1, 2)
        expt = 3
        self.assertEqual(res, expt)


if __name__ == '__main__':
    unittest.main(verbosity=2)