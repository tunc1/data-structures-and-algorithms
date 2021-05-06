import unittest
from linked_list import LinkedList

class LinkedListTest(unittest.TestCase):
    
    def setUp(self):
        self.list=LinkedList()

    def test_add(self):
        self.list.add(1)
        self.assertEqual(self.list.get_size(),1)
    
    def test_addMultiple(self):
        for i in range(4):
            self.list.add(i)
        self.assertEqual(self.list.get_size(),4)
    
    def test_add_to_index(self):
        self.list.add_to_index(5,0)
        self.assertEqual(self.list.get(0),5)
        self.list.add(1)
        self.list.add(3)
        self.list.add_to_index(2,1)
        self.assertEqual(self.list.get(1),2)
        self.list.add_to_index(0,0)
        self.assertEqual(self.list.get(0),0)
        self.list.add_to_index(4,4)
        self.assertEqual(self.list.get(4),4)
    
    def test_get(self):
        self.list.add_multiple(1,2,3)
        self.assertEqual(self.list.get(1),2)
    
    def test_get_last(self):
        self.list.add_multiple(1,2,3)
        self.assertEqual(self.list.get_last(),3)
    
    def test_get_first(self):
        self.list.add_multiple(1,2,3)
        self.assertEqual(self.list.get_first(),1)
    
    def test_remove(self):
        self.list.add_multiple(1,2,3,4,5)
        self.list.remove(1)
        self.assertEqual(self.list.get(1),3)
        self.list.remove(0)
        self.assertEqual(self.list.get(0),3)
    
    def test_remove_last(self):
        self.list.add_multiple(1,2,3,4,5)
        self.list.remove_last()
        self.assertEqual(self.list.get_last(),4)

    def test_pop(self):
        self.list.add_multiple(1,2,3)
        self.assertEqual(self.list.pop(),3)
        self.assertEqual(self.list.pop(),2)
    
    def test_get_size(self):
        self.assertEqual(self.list.get_size(),0)
        self.list.add_multiple(1,2,3)
        self.assertEqual(self.list.get_size(),3)
    
    def test_is_empty(self):
        self.assertTrue(self.list.is_empty())
        self.list.add_multiple(1,2,3)
        self.assertFalse(self.list.is_empty())

    def test_str(self):
        self.list.add(1)
        self.list.add(4)
        self.list.add(3)
        self.assertEqual(str(self.list),"[1,4,3]")