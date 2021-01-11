import binary_search
import unittest

class BinarySearchTest(unittest.TestCase):
    
    def test_search(self):
        array=[4,2,5,7,3,1]
        expected=1
        result=binary_search.search(array,2)
        self.assertEqual(expected,result)
        expected=-1
        result=binary_search.search(array,0)
        self.assertEqual(expected,result)