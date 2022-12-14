from connector import Connector


class Product:
    id: int
    title: str
    price: float
    count: int
    category: int

    def __init__(self, data_json):
        self.id = data_json.get('id')
        self.title = data_json.get('title')
        self.price = data_json.get('price')
        self.count = data_json.get('count')
        self.category = data_json.get('category')

    def __str__(self):
        return f'Продукт "{self.title}" с количеством на складе {self.count} с ценой {self.price} за кг'

    def __bool__(self):
        """
        Проверяет есть ли товар в наличии
        """
        return self.count

    def __len__(self):
        """
        Возвращает количество товара на складе
        """
        return self.count


class Category:
    id: int
    title: str
    description: str
    products: list

    def __init__(self, data_json):
        self.id = data_json.get('id', '')
        self.title = data_json.get('title','')
        self.description = data_json.get('description',)
        self.products = []

    def __str__(self):
        return f'Номер индефикатора {self.id} для категории {self.title} '

    def __bool__(self):
        """
        Проверяет есть ли товар в категории
        """
        return len(self.products)

    def __len__(self):
        """
        Возвращает количество наименований товаров, у которых есть наличие на складе
        """
        count = 0
        for i in self.products:
            if i.count > 0:
                count += 1
        return count


class Shop:
    """
    Класс для работы с магазином
    """

    # products: list
    # categories: list

    def __init__(self, *args, **kwargs):
        pass

    def get_categories(self):
        """
        Показать все категории пользователю в произвольном виде, главное, чтобы пользователь
        мог видеть идентификаторы (id) каждой категории
        """
        product_connector = Connector('categories.json')
        cat_list = product_connector.select({})

        for i in cat_list:
            cat_obj = Category(i)
            print(cat_obj)

    def get_products(self):
        """
        Запросить номер категории и вывести все товары, которые относятся к этой категории
        Обработать вариант отсутствия введенного номера
        """
        cat_number = input('Введите номер категории: ')

        while not cat_number.isdigit():
            cat_number = input('Введите НОМЕР категории, а не что-то другое: ')

        product_connector = Connector('products.json')
        products_list = product_connector.select({'category': int(cat_number)})
        for prod in products_list:
            prod_obj = Product(prod)
            print(prod_obj)

    def get_product(self):
        """
        Запросить ввод номера товара и вывести всю информацию по нему в произвольном виде
        Обработать вариант отсутствия введенного номера
        """
        cat_number = input('Введите номер товара : ')

        while not cat_number.isdigit():
            cat_number = input('Введите НОМЕР товара, а не что-то другое: ')

        product_connector = Connector('products.json')
        products_list = product_connector.select({'id': int(cat_number)})
        for prod in products_list:
            prod_obj = Product(prod)
            print(prod_obj)


if __name__ == '__main__':
    my_shop = Shop()
    my_shop.get_products()
    my_shop.get_product()
    my_shop.get_categories()
