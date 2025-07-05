import pytest

from src.objects import Category, Product


@pytest.fixture
def Product_Qq():
    return Product("Motorola", "Чудесный кнопочный", 1000.0, 1)


def test_Product(Product_Qq):

    assert Product_Qq.name == "Motorola"
    assert Product_Qq.description == "Чудесный кнопочный"
    assert Product_Qq.price == 1000


def test_Product_price_setter(capsys, Product_Qq):

    assert Product_Qq.price == 1000

    Product_Qq.price = 0  #
    message = capsys.readouterr()

    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    Product_Qq.price = 1001  # без фикстуры - можно менять
    assert Product_Qq.price == 1001

    Product_Qq.price = -1  #
    message = capsys.readouterr()

    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"

    # new_product() НЕ проверяем


@pytest.fixture
def Category_Qq():

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство для удобства жизни",
        [product1, product2],
    )

    return category1


def test_Category_ct(Category_Qq):
    assert Category_Qq.name == "Смартфоны"
    assert Category_Qq.description == "Смартфоны, как средство для удобства жизни"
    assert Category_Qq.category_count == 2
    assert Category_Qq.product_count == 13

    assert Category_Qq.products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
    ]

    p = Product("Motorola", "Чудесный кнопочный", 1000.0, 1)

    Category_Qq.add_product(p)

    assert Category_Qq.products == [
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.",
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.",
        "Motorola, 1000.0 руб. Остаток: 1 шт.",
    ]
    assert Category_Qq.products[2] == "Motorola, 1000.0 руб. Остаток: 1 шт."
