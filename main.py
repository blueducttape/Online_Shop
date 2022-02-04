from typing import Any


class Shop:
    """
    Класс "Магазин"
    """
    def __init__(self, shop_name: str = None):
        self.shop_name = shop_name
        self._user = []
        self._product_list = []
        self._categories = []


class Product(Shop):
    """
    Класс "Товар"
    """
    def __init__(self, name: str, price: [int, float] = 1, rating: float = 1.0):
        self.name = name    # название
        self.price = price  # цена
        self.rating = rating    # рейтинг товара

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.price},{self.rating})"

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price}, Рейтинг: {self.rating}"


class Category(Shop):
    """
    Класс "Категория", описывает категорию товара
    """
    def __init__(self, name: str, product_array: list[Product] = []):
        self._cat_id = Category.next_id = Category.next_id + 1
        self._product_array = []
        self.name = name    # название категории товаров
        self.product_array = product_array  # массив с товарами

    def __str__(self):
        items_string = '\t'
        for item in self.product_array:
            items_string += str(item) + '\n\t'
        return f"В категории {self.name} следующие товары: \n{items_string}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.product_array})"


class Basket(Shop):
    """
    Класс "Корзина"
    """

    def __init__(self, product: Product = None):
        self._order_array = []
        if product is not None:
            self.add_to_cart(product)

    def __str__(self):
        items_string = '\t'
        for item in self.order_array:
            items_string += str(item) + '\n\t'
        return f"Товары в корзине: \n{items_string}" if self.order_array else "В корзине пусто"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._order_array[0]})" if self._order_array else f"{self.__class__.__name__}(None)"


class User:
    """
    Класс, описывающий пользователя
    """
    def __init__(self, login: str, password: Any = None, user_basket: Basket = None):
        self.login = login  # логин
        self.password = password    # пароль
        self.basket = user_basket   # корзина пользователя

    def __repr__(self):
        pass_str = self.password if self.password else None
        basket_str = self.basket if self.basket else None
        return f"{self.__class__.__name__}({self.login}, {pass_str}, {basket_str})"

    def __str__(self):
        return f"Пользователь {self.login}, товаров в корзине: {str(self.basket)}"

    @property
    def password(self) -> str:
        return self._password


if __name__ == '__main__':
    user1 = User("Александр22", "123456", " ")
    print (user1)
