import unittest
from src.item import Item

class TestItem(unittest.TestCase):
    def test_calculate_total_price(self):
        item = Item("Тестовый товар", 100, 3)
        self.assertEqual(item.calculate_total_price(), 300)

    def test_apply_discount(self):
        item = Item("Тестовый товар", 100, 1)
        Item.pay_rate = 0.9  # устанавливаем уровень цен с учетом 10% скидки
        item.apply_discount()
        self.assertEqual(item.price, 90)

if __name__ == '__main__':
    unittest.main()
