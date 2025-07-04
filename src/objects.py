class Product:
    """класс для представления Продукта"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    """класс для представления Категории"""

    product_count: int = 0  # аттрибут класса :: счетчик Продуктов в категории
    category_count: int = 0  # аттрибут класса ::счетчик экземпляров в категории

    name: str
    description: str
    __products: list[Product]

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        for p in self.__products:
            Category.product_count += p.quantity
        # аттрибут класса :: счетчик Продуктов в категории
        Category.category_count += len(self.__products)
        # аттрибут класса ::счетчик экземпляров в категории
