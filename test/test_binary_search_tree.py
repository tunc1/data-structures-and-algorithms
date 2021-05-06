import unittest
from binary_search_tree import BinarySearchTree

class BinarySearchTreeTest(unittest.TestCase):
    
    def test_insert(self):
        tree=BinarySearchTree()
        array=[5,1,7,4,3,6,9,10,19,15]
        for item in array:
            tree.insert(item)
        self.assertEqual(tree.root.right.left.data,6)
    
    def test_search(self):
        tree=BinarySearchTree()
        array=[5,1,7,4,3,6,9,10,19,15]
        for item in array:
            tree.insert(item)
        self.assertEqual(tree.search(3),True)
        self.assertEqual(tree.search(8),False)