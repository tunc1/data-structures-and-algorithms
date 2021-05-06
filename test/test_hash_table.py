from unittest import TestCase
from hash_table import HashTable

class HashTableTest(TestCase):
    
    def setUp(self):
        self.hash_table=HashTable(3)

    def test_insert(self):
        self.hash_table.insert("1",1)
        self.assertEqual(self.hash_table.get("1"),1)

    def test_get(self):
        self.hash_table.insert("1",1)
        self.assertEqual(self.hash_table.get("1"),1)

    def test_delete(self):
        self.hash_table.insert("1",1)
        self.hash_table.delete("1")
        self.assertEqual(self.hash_table.get("1"),None)