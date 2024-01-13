import unittest
from src.item import Item

class TestItem(unittest.TestCase):
    def test_repr(self):
        item = Item("Тестовый товар", 100, 3)
        self.assertEqual(repr(item), "Item('Тестовый товар', 100, 3)")

    def test_str(self):
        item = Item("Тестовый товар", 100, 3)
        self.assertEqual(str(item), "Тестовый товар")

if __name__ == '__main__':
    unittest.main()