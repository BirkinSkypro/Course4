# Домашняя работа по ООП
урок 15.1 


## Описание:

  Это веб-приложение на Python для управления задачами и проектами.
  добавлены в  модуль src/objects классы :
  
class Product:
    """класс для представления Продукта"""

    name: str
    description: str
    __price: float
    quantity: int

  
class Category:
    """класс для представления Категории"""

    product_count: int = 0  # аттрибут класса :: счетчик Продуктов в категории
    category_count: int = 0  # аттрибут класса ::счетчик экземпляров в категории

    name: str
    description: str
    __products: list[Product]



## Установка (macOS):

1. Установите зависимости:

### 1.1 Вместо XCode установите Xcode Command Line Tools
    (он значительно меньше)
    Для каждоой версии macOS существует свои совместимые версии CLT)
    https://guide.macports.org/

###  1.2 Вместо HomeBrew установите macports (последнеюю версию*.dmg)
    
    обновите Macports:
    sudo port selfupdate
    sudo port upgrade outdated
    sudo port install poetry

### 1.3 установите пакеты внутри poetry:

    poetry add pytest black flake8 isort mypy pytest-cov
	
2. Клонируйте репозиторий: 
   пропишите в PyCharm в меню Git/Manage remote:

    URL:
    git://github.com/BirkinSkyPro/course4.git

    выполните в терминале проекта : git pull origin feature/homework14_2

## Тестирование:
```
запустите pytest (в корне проекта)
а также   pytest --cov=src --cov-report=html
для проверки покрытия тестами
```

## Использование классов модуля objects:

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

