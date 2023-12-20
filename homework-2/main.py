import csv
import os

class Item:
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

    def calculate_total_price(self) -> float:
        return self.price * self.quantity

    def apply_discount(self) -> None:
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_data(cls, data):
        items = [cls(row['name'], float(row['price']), int(row['quantity'])) for row in data]
        cls.all = items

    @staticmethod
    def string_to_number(value):
        return int(float(value))

# Пример использования
data = [
    {"name": "Телефон", "price": 10000, "quantity": 5},
    {"name": "Планшет", "price": 15000, "quantity": 3},
    # Другие товары
]

Item.instantiate_from_data(data)
assert len(Item.all) == len(data)