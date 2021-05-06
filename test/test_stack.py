import unittest
from stack import Stack

class StackTest(unittest.TestCase):
    
    def setUp(self):
        self.stack=Stack(5)

    def test_push(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(),1)
    
    def test_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        self.assertEqual(self.stack.pop(),2)
        self.assertEqual(self.stack.pop(),1)
    
    def test_top(self):
        self.stack.push(2)
        self.stack.push(1)
        self.assertEqual(self.stack.top(),1)
        self.assertEqual(self.stack.top(),1)
    
    def test_size(self):
        self.stack.push(1)
        self.assertEqual(self.stack.size(),1)
        self.stack.push(2)
        self.assertEqual(self.stack.size(),2)
    
    def test_is_empty(self):
        self.assertTrue(self.stack.is_empty())
        self.stack.push(1)
        self.assertFalse(self.stack.is_empty())