import unittest
from queue import Queue

class QueueTest(unittest.TestCase):
    
    def setUp(self):
        self.queue=Queue()

    def test_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(),1)
        self.assertEqual(self.queue.peek(),1)
    
    def test_dequeue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.dequeue(),1)
    
    def test_peek(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.peek(),1)
    
    def test_str(self):
        self.queue.enqueue(1)
        self.queue.enqueue(4)
        self.queue.enqueue(3)
        self.assertEqual(str(self.queue),"[1,4,3]")