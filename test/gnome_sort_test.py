from unittest import TestCase
from gnome_sort import sort

class GnomeSortTest(TestCase):

    def test_sort(self):
        array=[1,6,4,7,9,5,3,6,8,0,10,2]
        expected=[0,1,2,3,4,5,6,6,7,8,9,10]
        print(expected)
        self.assertEqual(expected,sort(array))