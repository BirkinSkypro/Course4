import pytest
from src.objects import Product, Category


@pytest.fixture
def Product_Qq():
    return Product("Motorola", "Чудесный кнопочный", 1000.0, 1)


def test_Product(Product_Qq):
    assert Product_Qq.name == "Motorola"
    assert Product_Qq.description == "Чудесный кнопочный"


@pytest.fixture
def Category_Qq():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство для удобства жизни",
        [product1, product2],
    )

    return category1


def test_Category(Category_Qq):
    assert Category_Qq.name == 'Смартфоны'
    assert Category_Qq.description == "Смартфоны, как средство для удобства жизни"
    assert Category_Qq.category_count == 2
    assert Category_Qq.product_count == 13
