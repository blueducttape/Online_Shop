from typing import Any


class Product:
    """Класс для описания товара
        :param name: название товара
        :param price: цена за единицу товара
        :param rate: рейтинг товара
        :param cat_id: номер категории
    """
    uid = 0

    def __init__(self, name: str, price: [int, float] = 1, rate: float = 1.0, cat_id: int = 0) -> None:
        self.name = name
        self.price = price
        self.rate = rate
        self.cat_id = cat_id

        self._uid = Product.uid = Product.uid + 1

    def __str__(self) -> str:
        return f"Товар: {self.name}, цена: {self.price}, рейтинг: {self.rate}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name},{self.price},{self.rate},{self.cat_id})"

    @staticmethod
    def _check_type(_object: Any, _type: type) -> Any:
        if not isinstance(_object, _type):
            raise TypeError(f"Ожидается {_type}, получено {type(_object)}")

    @property
    def cat_id(self) -> int:
        return self._cat_id

    @cat_id.setter
    def cat_id(self, id: int) -> int:
        self._check_type(id, int)
        self._cat_id = id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._check_type(name, str)
        self._name = name

    @property
    def price(self) -> [int, float]:
        return self._price

    @price.setter
    def price(self, price: [int, float]) -> None:
        self._check_type(price, (int, float))
        self._price = price

    @property
    def rate(self) -> [int, float]:
        return self._rate

    @rate.setter
    def rate(self, rate: [int, float]) -> None:
        self._check_type(rate, (int, float))
        self._rate = rate


class Category:
    """
    Класс для описания категории товара
        :param name: название категории
        :param product_array: массив товаров
    """
    next_id = 0

    def __init__(self, name: str, product_array: list[Product] = []) -> None:

        self._cat_id = Category.next_id = Category.next_id + 1
        self._product_array = []
        self.name = name
        self.product_array = product_array

    def __str__(self):
        items_string = '\t'
        for item in self.product_array:
            items_string += str(item) + '\n\t'
        return f"Товары в категории {self.name}: \n{items_string}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name},{self.product_array})"

    @property
    def id(self) -> int:
        return self._cat_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        Product._check_type(name, str)
        self._name = name

    @property
    def product_array(self) -> list[Product]:
        return self._product_array

    @product_array.setter
    def product_array(self, *args: Product) -> None:
        """
        установка значений товаров из категории
        :param product: объект типа Product или list[Product]
        """
        for item in args:
            if item:
                Product._check_type(item, Product)
                item.cat_id = self.id
                self._product_array.append(item)


class Basket:
    """
    Класс для описания корзины
    """

    def __init__(self, product: Product = None):
        self._order_array = []
        if product is not None:
            self.add_to_cart(product)

    def __str__(self):
        items_string = '\t'
        for item in self.order_array:
            items_string += str(item) + '\n\t'
        return f"Товар в корзине: \n{items_string}" if self.order_array else "корзина пуста"

    def __repr__(self):
        return f"{self.__class__.__name__}({self._order_array[0]})" if self._order_array else f"{self.__class__.__name__}(None)"

    @property
    def order_array(self) -> list[Product]:
        return self._order_array

    def add_to_cart(self, product: Product) -> None:
        """
        установка значений товаров из категории
        :param product: объект типа Product
        """
        Product._check_type(product, Product)
        self._order_array.append(product)


class User:
    """
    Класс "Покупатель"
        :param login: Логин пользователя
        :param password: Пароль пользователя
        :param user_basket: Корзина пользователя
    """
    default_pass = '12345'   # пароль по умолчанию

    def __init__(self, login: str, password: Any = None, user_basket: Basket = None):
        self.login = login
        self.password = password
        self.basket = user_basket

    def __str__(self) -> str:
        return f"Пользователь {self.login}, {str(self.basket)}"

    def __repr__(self) -> str:
        pass_str = self.password if self.password else None
        basket_str = self.basket if self.basket else None
        return f"{self.__class__.__name__}({self.login}, {pass_str}, {basket_str})"

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, new_pass: Any = None) -> None:
        """
        Установка нового пароля пользователя
        :param new_pass: новое значение
        """
        if new_pass and isinstance(new_pass, (str, int, float)):
            self._password = new_pass
        else:
            print("Установлен пароль по умолчанию")
            self._password = self.default_pass

    @property
    def basket(self) -> Basket:
        return self._basket

    @basket.setter
    def basket(self, basket: Basket = None) -> None:
        if basket:
            self._basket = basket
        else:
            self._basket = Basket()


class Shop:
    """
    Основной класс интернет-магазина
    """
    def __init__(self):
        self._user = []             # список пользователей магазина
        self._product_list = []     # список товаров в магазине
        self._categories = []       # список категорий товаров и магазине
        self._current_user = None        # текущий пользователь

    def user(self) -> list[User]:
        """ Список пользователей"""
        return self._user

    def add_user(self, new_user: User = None) -> None:
        """
        Добавление пользователя в интернет-магазин
        :param new_user: добавляемый пользователь
        """
        print("Регистрация нового пользователя")
        if new_user:
            Product._check_type(new_user, User)
        else:
            user_name = self._input_user_data('имя пользователя (логин)')
            user_pass = self._input_user_data('пароль')
            new_user = User(user_name, user_pass)
        self._user.append(new_user)

    def _input_user_data(self, print_string: str) -> str:
        """
        Ввод данных пользователя
        :return: Возвращает введенную строку
        """
        return str(input(f"Введите {print_string}: "))

    def _search_user(self, user_name: str) -> [User, None]:
        """
        Поиск пользователя по его имени среди зарегистрированных
        :param user_name: искомое имя пользователя
        :return: объект User, если пользователь был зарегистрирован ранее, иначе None
        """
        for user in self._user:
            if user.login == user_name:
                return user
        return None

    def authentication(self) -> None:
        """Авторизация пользователя в магазине"""
        print("Авторизация пользователя")
        user = self._search_user(self._input_user_data('имя пользователя (логин)'))
        if not user:
            raise ValueError('пользователя с таким именем не существует')
        passwd = self._input_user_data(f'пароль пользователя {user.login}')
        if not passwd == user.password:
            raise ValueError('Неверный пароль!')
        self._current_user = user

    @property
    def cur_user(self) -> User:
        return self._current_user

    @cur_user.setter
    def cur_user(self, user: User = None) -> None:
        """Установка текущего пользователя"""
        Product._check_type(user, User)
        self._current_user = user

    def print_product_list(self) -> str:
        """Возвращает "строку" с перечнем товаров в магазине"""
        result = ' '
        for item in self._product_list:
            result += f'\t{item}\n'
        return result

    def _add_category_to_list(self, new_cat: Category) -> [Category, None]:
        """Добавление категории в список категорий"""
        Product._check_type(new_cat, Category)
        self._categories.append(new_cat)

    def _add_categories_to_list(self, *args: Category) -> None:
        """Добавление категорий в список"""
        for cat in args:
            self._add_category_to_list(cat)

    def create_new_category(self) -> None:
        """создание новой категории"""
        name = self._input_user_data('название категории')
        self._add_category_to_list(Category(name))

    def _search_category_id_in_list(self, id: int) -> [Category, None]:
        """
        Поиск по категории по id
        :param id: искомый id
        :return: объект Category или None
        """
        Product._check_type(id, int)
        for cat in self._categories:
            if cat.id == id:
                return cat
        return None

    def _search_category_name_in_list(self, name: str) -> [Category, None]:
        """
        Поиск по категории по названию
        :param name: искомое название
        :return: объект Category или None
        """
        Product._check_type(name, str)
        for cat in self._categories:
            if cat.name == name:
                return cat
        return None

    def add_products_to_category(self, *args, **kwargs) -> None:
        """Добавление продуктов в категорию"""
        for key in kwargs:
            if key == "id":
                cat = self._search_category_id_in_list(kwargs[key])
            if key == "name":
                cat = self._search_category_name_in_list(kwargs[key])
        for product in args:
            Product._check_type(product, Product)
            product.cat_id = cat.id
            cat.product_array = product

    def print_categories_list(self) -> str:
        """Вывод списка категорий"""
        result = ''
        for cat in self._categories:
            result += f"\tid{cat.id} {cat.name}"
        return result

    def print_category_with_products(self) -> str:
        """Вывод списка товаров, разбитых по категориям"""
        result = ''
        for cat in self._categories:
            result += f'{cat.name}\n'
            for product in cat.product_array:
                result += f'\t{str(product)}\n'
        return result

    def add_to_cart(self, product: Product) -> None:
        """Добавление товара в корзину"""
        self.cur_user.basket.add_to_cart(product)
        print(Basket(product))

    def check_order(self) -> str:
        """Вычисление суммы заказа"""
        total_cost = 0
        for item in self.cur_user.basket.order_array:
            total_cost += item.price
        print(f"К оплате {total_cost} руб.")


if __name__ == '__main__':
    shop = Shop()
    shop.add_user()
    shop.authentication()
    # добавляем новую категорию
    shop._add_categories_to_list(Category('Молочная продукция'), Category('Хлебобулочные изделия'), Category('Овощи'))
    # создаем новую категорию
    # shop.create_new_category()
    # добавляем товары в категории
    shop.add_products_to_category(Product('Кефир', 40, 4.0),
                                  Product('Молоко', 35, 5.0), Product('Ряженка', 50, 5.0), id=1)
    shop.add_products_to_category(Product("Хлеб", 34, 4.3),
                                  Product("Печенье", 75, 4.9), Product("Бисквит", 60, 5.0), id=2)
    shop.add_products_to_category(Product("Помидоры", 66, 4.8), Product("Картофель", 50, 4.9),
                                  Product("Огурцы", 77, 5.0), id=3)
    # вывод товаров с категориями
    print(shop.print_category_with_products())
    # добавляем товары в корзину
    shop.add_to_cart(Product('Кефир', 100, 4.0))
    shop.add_to_cart(Product('Молоко', 35, 5.0))
    # вывод общей суммы покупки
    shop.check_order()    # создадим еще одного юзера
    shop.print_product_list()
    shop.add_user()
    shop.authentication()
    shop.user()
    shop.add_to_cart(Product("Огурцы", 77.0, 5.0))
    shop.add_to_cart(Product("Помидоры", 66.0, 4.8))
    shop.check_order()




