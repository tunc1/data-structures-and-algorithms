from unittest import TestCase
from bubble_sort import sort

class BubbleSortTest(TestCase):

    def test_sort(self):
        array=[4,6,2,1,8,0,4,2,4]
        expected=[0,1,2,2,4,4,4,6,8]
        self.assertEqual(sort(array),expected)