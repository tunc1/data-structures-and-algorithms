from unittest import TestCase
from selection_sort import sort

class SelectionSortTest(TestCase):

    def test_sort(self):
        array=[5,3,2,54,6,5,3,6,8,5,3,1,4]
        expected=[1,2,3,3,3,4,5,5,5,6,6,8,54]
        self.assertEqual(expected,sort(array))