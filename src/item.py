import csv
import os

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0  # уровень цен (по умолчанию без скидки)
    all = []  # список созданных экземпляров

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @staticmethod
    def string_to_number(value):
        return int(float(value))

    @classmethod
    def instantiate_from_csv(cls, data):
        cls.all.clear()
        filepath = os.path.abspath(__file__)
        parent_directory = os.path.dirname(os.path.dirname(filepath))
        full_path = os.path.join(parent_directory, data)
        with open(full_path, "r", encoding="windows-1251") as file:
            reader = csv.DictReader(file)
            items = list(reader)
        for item in items:
            Item(
                name=item['name'],
                price=float(item['price']),
                quantity=int(item['quantity']),
            )
    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name