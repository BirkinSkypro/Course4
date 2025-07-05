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

        return Product(**dict_product)  # распаковка kwargs

    # Геттер для __price
    @property
    def price(self):

        return self.__price

    @price.setter
    def price(self, price_new):
        if price_new <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = price_new

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."


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

        if isinstance(product, Product):

            self.__products.append(product)
            Category.product_count += product.quantity

    # Геттер для __products
    @property
    def products(self):

        ret = []
        # print(f"getter for {len(self.__products)}")
        for product in self.__products:

            out = ""

            out += str(product)

            ret.append(out)

        return ret

    def __str__(self):

        count=0
        out="Название категории, количество продуктов: 200 шт."
        for product in self.__products:

            count += product.quantity

            ret.append(out)

        return ret