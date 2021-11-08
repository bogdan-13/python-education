import json
import os.path


class Menu:

    def __init__(self):
        self.__menu_items = dict()

    def add_item(self, item, item_price) -> None:
        with open('data/menu.json', 'r', encoding='utf-8') as file:
            self.__menu_items = json.load(file)

        self.__menu_items[item] = item_price

        with open('data/menu.json', 'w', encoding='utf-8') as file:
            json.dump(self.__menu_items, file, indent=4, ensure_ascii=False)

    def del_item(self, item) -> None:
        with open('data/menu.json', 'r', encoding='utf-8') as file:
            self.__menu_items = json.load(file)

        try:
            self.__menu_items.pop(item)
        except KeyError:
            pass
        with open('data/menu.json', 'w', encoding='utf-8') as file:
            json.dump(self.__menu_items, file, indent=4, ensure_ascii=False)

    def display_menu(self):
        with open('data/menu.json', 'r', encoding='utf-8') as file:
            self.__menu_items = json.load(file)

        for key, value in self.__menu_items.items():
            print(f'{key}: {value} грн.')

    @property
    def menu_items(self):
        with open('data/menu.json', 'r', encoding='utf-8') as file:
            return json.load(file)


class Storage:
    def __init__(self):
        self.__products = dict()

    @property
    def products(self):
        with open('data/storage.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def add_item(self, item, item_number) -> None:
        with open('data/storage.json', 'r', encoding='utf-8') as file:
            self.__products = json.load(file)

        try:
            self.__products[item] += item_number
        except KeyError:
            self.__products[item] = item_number

        with open('data/storage.json', 'w', encoding='utf-8') as file:
            json.dump(self.__products, file, indent=4, ensure_ascii=False)

    def del_item(self, item) -> None:
        with open('data/storage.json', 'r', encoding='utf-8') as file:
            self.__products = json.load(file)
        try:
            self.__products.pop(item)
        except KeyError:
            print('Даний інгридієнт відсутній на складі')
        with open('data/storage.json', 'w', encoding='utf-8') as file:
            json.dump(self.__products, file, indent=4, ensure_ascii=False)

    def get_item(self, item, amount):
        with open('data/storage.json', 'r', encoding='utf-8') as file:
            self.__products = json.load(file)
        if self.__products[item] - amount >= 0:
            self.__products[item] -= amount
            with open('data/storage.json', 'w', encoding='utf-8') as file:
                json.dump(self.__products, file, indent=4, ensure_ascii=False)
            return item, amount
        else:
            raise ValueError


class Order:

    def __init__(self, order_id, owner_name):
        self.owner_name = owner_name
        self.order_id = order_id
        self.__order_items = dict()
        self.__delivery_address = ''
        self.__order_status = None
        self.order_content = {'owner_name': owner_name,
                              'order_id': order_id,
                              'delivery_address': self.__delivery_address,
                              'order_items': self.__order_items}

    @property
    def order_items(self):
        return self.order_content['order_items']

    @property
    def delivery_address(self):
        return self.order_content['delivery_address']

    @property
    def order_status(self):
        for path in os.walk('data/orders'):
            if f'{self.owner_name}.{self.order_id}.json' in path[2]:
                _, _, self.__order_status = path[0].split('/')
        return self.__order_status

    def add_item(self, item, number_portions):
        self.order_content['order_items'].update([(item, number_portions)])

    def remove_item(self, item):
        self.order_content['order_items'].pop(item, None)

    def add_address(self, address):
        self.order_content['delivery_address'] = address

    def price_order(self, menu):
        price = 0
        for key in self.order_items:
            if key in menu.menu_items:
                price += menu.menu_items[key] * self.order_items[key]
        return price

    def order_action(self, order_action):
        if not os.path.exists(f'data/orders/{order_action}'):
            os.mkdir(f'data/orders/{order_action}')
        if self.order_status and self.order_status != order_action:
            os.rename(f'data/orders/{self.order_status}/{self.owner_name}.{self.order_id}.json',
                      f'data/orders/{order_action}/{self.owner_name}.{self.order_id}.json')
        else:
            with open(f'data/orders/{order_action}/'
                      f'{self.owner_name}.{self.order_id}.json', 'w', encoding='utf-8') as file:
                json.dump(self.order_content, file, indent=4, ensure_ascii=False)


class Employee:
    @staticmethod
    def show_menu(menu):
        menu.display_menu()

    @staticmethod
    def get_order(order_id, owner_name):
        order = Order(order_id, owner_name)
        if order.order_status:
            with open(f'data/orders/{order.order_status}/'
                      f'{owner_name}.{order_id}.json', 'r', encoding='utf-8') as file:
                order.order_content = json.load(file)
            return order
        else:
            raise FileNotFoundError

    @staticmethod
    def get_last_id():
        orders_list = []
        for _, _, files in os.walk(f'data/orders'):
            for order in files:
                orders_list.append(order)
        if orders_list:
            _, last_id, _ = max(orders_list).split('.')
            return int(last_id)
        else:
            return 0

    def get_current_order(self, order_status):
        orders_list = []
        for _, _, files in os.walk(f'data/orders/{order_status}'):
            for order in files:
                orders_list.append(order)
        if orders_list:
            owner_name, first_id, _ = min(orders_list).split('.')
            return self.get_order(first_id, owner_name)


class ServiceStaff(Employee):
    def __init__(self, name):
        self.name = name

    def create_order(self, menu):

        order_id = self.get_last_id() + 1
        order = Order(order_id, self.name)

        print('Введіть замовлення, щоб закінчити натисніть "enter"')
        while True:
            order_item = input('Введіть назву страви: ')
            if order_item == '':
                break
            if order_item in menu.menu_items:
                number_portions = int(input('Введіть кількість порцій: '))
                order.add_item(order_item, number_portions)
            else:
                print('Нажаль такої страви немає в меню')

        print(f'id вашого замовлення №{order_id}')

        if isinstance(self, OnlineManager):
            address = input('Ввкдіть адресу доставки: ')
            order.add_address(address)

        order.order_action('created')

        return order

    @staticmethod
    def update_order(order, menu):
        no_possible = order.order_content.pop('no_cook', [])
        for item in no_possible:
            order.remove_item(item)

        while True:
            order_item = input('Введіть назву страви: ')
            if order_item == '':
                break
            if order_item in menu.menu_items:
                number_portions = int(input('Введіть кількість порцій: '))
                order.add_item(order_item, number_portions)
            else:
                print('Нажаль такої страви немає в меню')
            order.order_action(order.order_status)
            order.order_action('created')


class Waiter(ServiceStaff):

    def serve_order(self, order):
        if order.owner_name == self.name:
            if order.order_status == 'ready':
                order.order_action('served')
            else:
                print(f'Замовлення №{order.order_id} ще не готове')
        else:
            print('Це замовлення іншого офіціанта')

    def accept_payment(self, order):
        if order.owner_name == self.name:
            order.order_action('paid')
        else:
            print('Це замовлення іншого офіціанта')


class OnlineManager(ServiceStaff):

    @staticmethod
    def to_delivery(order):
        if order.delivery_address:
            if order.order_status == 'ready':
                order.order_action('to_delivery')
            else:
                print(f'Замовлення №{order.order_id} ще не готове')
        else:
            print('Це замовлення з залу')


class Courier(Employee):

    def delivery_order(self):
        order = self.get_current_order('to_delivery')
        if order:
            order.order_action('delivered')
            print(f'Замовлення № {order.order_id} доставлено за адресою: {order.delivery_address}')
        else:
            print('Немає замовлень в черзі на доставку.')


class Cook(Employee):
    @staticmethod
    def show_order(order):
        print('Замовлено:')
        for item in order.order_items.items():
            key, value = item
            print(f'{key} - {value} порцій')

    @staticmethod
    def to_cook(order, storage):
        taken_ingredients = []
        is_complete = True
        with open('data/recipes.json', 'r', encoding='utf-8') as file:
            recipes = json.load(file)
        no_cook = []
        for dish, portions in order.order_items.items():
            print(f'Готується {dish} в кількості {portions} порцій')

            for ingredient in recipes[dish]:
                ingredient_amount = recipes[dish][ingredient] * portions
                try:
                    item, amount = storage.get_item(ingredient, ingredient_amount)
                    taken_ingredients.append((item, amount))
                except ValueError:
                    is_complete = False
                    no_cook.append(dish)
                    print(f'Недостатньо {ingredient} на складі')
                    print(f'Залишок {ingredient} на складі - {storage.products[ingredient]},'
                          f' потрібно - {ingredient_amount}')
                    break
                except KeyError:
                    is_complete = False
                    no_cook.append(dish)
                    print(f'Hа складі відсутній {ingredient}')
                    break
        order.order_content['no_cook'] = no_cook
        if is_complete:
            for item in taken_ingredients:
                key, value = item
                print(f'Взято зі складу {key} - {value}')
            print('Замовлення готове :)')
            order.order_action(order.order_status)
            order.order_action('ready')
        else:
            print('Замовлення не готове :(')
            for item in taken_ingredients:
                key, value = item
                storage.get_item(key, -value)
            order.order_action(order.order_status)
            order.order_action('returned')


class Chef:
    @staticmethod
    def create_recipe(recipe_name):
        ingredients = dict()

        while True:
            ingredient = input('Введіть назву продукту (для завершення натисніть "enter"): ')
            if ingredient == '':
                break
            ingredients[ingredient] = float(input('Введіть кількість: '))

        with open('data/recipes.json', 'r', encoding='utf-8') as file:
            recipes = json.load(file)

        recipes.update([(recipe_name, ingredients)])

        with open(f'data/recipes.json', 'w', encoding='utf-8') as file:
            json.dump(recipes, file, indent=4, ensure_ascii=False)

    @staticmethod
    def update_menu(menu):
        while True:
            menu_item = input('Введіть назву страви (для завершення натисніть "enter"): ')
            if menu_item == '':
                break
            item_price = int(input('Введіть ціну за порцію: '))
            menu.add_item(menu_item, item_price)

    @staticmethod
    def update_storage(storage):
        while True:
            item = input('Введіть назву продукту (для завершення натисніть "enter"): ')
            if item == '':
                break
            item_number = int(input('Введіть кількість: '))
            if item in storage.products:
                item_number = storage.products[item] + item_number
                storage.add_item(item, item_number)
            else:
                storage.add_item(item, item_number)
