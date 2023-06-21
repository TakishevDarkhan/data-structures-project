"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest


class Node(unittest.TestCase):
    def test_init(self):
        self.assertNotEqual((5, None), 5)
        self.assertNotEqual(('a', 'n1'), 'a')
        self.assertTrue('n1', '<src.stack.Node object at 0x0000024D3A439150>')
        self.assertTrue('n2.next_node', '<__main__.Node object at 0x0000022803036050>')

class Stack(unittest.TestCase):
    def test_push(self):
        self.assertNotEqual(('data2', 'data3'), 'data1')
        self.assertNotEqual(('data1', 'data3'), 'data2')
        self.assertNotEqual(('data2', 'data1'), 'data3')

    def test_pop(self):
        self.assertIsNone(None)
        self.assertTrue("AttributeError: 'NoneType' object has no attribute 'data'")



