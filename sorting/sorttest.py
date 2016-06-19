from mergesort import *
from quicksort import *
import random
import unittest

class TestSort(unittest.TestCase):
    def test_mergesort(self):
        testlist = [random.randrange(0, 10000) for _ in range(2001)]
        self.assertEqual(mergesort(testlist), sorted(testlist))

    def test_quicksort(self):
        testlist = [3, 4, 2, 1, 8, 7]
        #testlist = [random.randrange(0, 10000) for _ in range(2001)]
        self.assertEqual(quicksort(testlist), sorted(testlist))

if __name__ == '__main__':
    unittest.main()
