from unittest import TestCase
from counting_sort import sort

class CountingSortTest(TestCase):
    
    def test_sort(self):
        array=[6,0,4,2,3,5,10,4,8,4,2,1,5,7,8]
        self.assertEqual(sort(array),[0,1,2,2,3,4,4,4,5,5,6,7,8,8,10])