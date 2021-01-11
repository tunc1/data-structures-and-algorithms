import unittest
import linear_search

class LinearSearchTest(unittest.TestCase):
    
    def test_search(self):
        array=[3,5,2,1,7,6]
        expected=2
        result=linear_search.search(array,2)
        self.assertEqual(expected,result)
        expected=-1
        result=linear_search.search(array,0)
        self.assertEqual(expected,result)