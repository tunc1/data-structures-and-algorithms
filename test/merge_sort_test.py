import merge_sort
import unittest

class MergeSortTest(unittest.TestCase):
    
    def test_sort(self):
        array=[1,5,6,3,2,1,0]
        merge_sort.sort(array)
        self.assertEqual(array,[0,1,1,2,3,5,6])