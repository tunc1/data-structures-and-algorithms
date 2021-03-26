from unittest import TestCase
from insertion_sort import sort

class InsertionSortTest(TestCase):

    def test_sort(self):
        array=[0,5,1,9,4,0,2,4]
        expected=[0,0,1,2,4,4,5,9]
        self.assertEqual(expected,sort(array))