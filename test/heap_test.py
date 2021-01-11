import unittest
from heap import *

class MaxHeapTest(unittest.TestCase):
    
    def setUp(self):
        self.heap=MaxHeap()
    
    def test_insert(self):
        array=[35,33,42,10,14,19,27,44,26,31]
        for item in array:
            self.heap.insert(item)
        self.assertEqual(str(self.heap),"[44, 42, 35, 33, 31, 19, 27, 10, 26, 14]")
    
    def test_remove(self):
        array=[35,33,42,10,14,19,27,44,26,31]
        for item in array:
            self.heap.insert(item)
        self.heap.remove()
        self.assertEqual(str(self.heap),"[42, 33, 35, 26, 31, 19, 27, 10, 14]")

class MinHeapTest(unittest.TestCase):
    
    def setUp(self):
        self.heap=MinHeap()
    
    def test_insert(self):
        array=[3,9,2,1,4,5]
        for item in array:
            self.heap.insert(item)
        self.assertEqual(str(self.heap),"[1, 2, 3, 9, 4, 5]")
    
    def test_remove(self):
        array=[3,9,2,1,4,5]
        for item in array:
            self.heap.insert(item)
        self.heap.remove()
        self.assertEqual(str(self.heap),"[2, 4, 3, 9, 5]")