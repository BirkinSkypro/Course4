class Product:
    """класс для представления Продукта"""

    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, dict_product: dict):
        """создание экземпляра по словарю"""
        return Product(**dict_product)  # распаковка kwargs

    # Геттер для __price
    @property
    def price(self):
        """чтение private аттрибута"""
        return self.__price

    @price.setter
    def price(self, price_new):
        """запись в private аттрибут"""
        if price_new <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price_new

    def __str__(self):
        """приведение к строке (__magic__ method)"""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, prod) -> float:
        """сложение (__magic__ method)"""

        summa = self.price * self.quantity
        if isinstance(prod, Product):
            summa += prod.price * prod.quantity
        return summa


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

    def add_product(self, product: Product):
        """добавление продукта в категорию"""
        if isinstance(product, Product):

            self.__products.append(product)
            Category.product_count += product.quantity

    # Геттер для __products
    @property
    def products(self):
        """чтение private аттрибута __products"""
        ret = []
        for product in self.__products:

            ret.append(str(product))

        return ret

    def __str__(self):
        """приведение к строке (__magic__ method)"""

        out = f"{self.name}, количество продуктов: {Category.product_count} шт."

        return out
