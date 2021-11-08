from restaurant_lib import Menu, Waiter

while True:
    menu_item = input('Оберіть пункт меню: '
                      '\n1. Прийняти замовлення'
                      '\n2. Скоригувати замовлення з черги'
                      '\n3. Обслужити замовлення з черги'
                      '\n4. Прийняти оплату'
                      '\n5. Вихід \n')
    if menu_item in ('1', '2', '3', '4', '5'):
        break
name = input('Введіть своє імʼя: ')
waiter = Waiter(name)
menu = Menu()

if menu_item == '1':
    waiter.show_menu(menu)
    waiter.create_order(menu)
elif menu_item == '2':
    order = waiter.get_current_order('returned')
    if order:

        waiter.update_order(order, menu)
    else:
        print('Немає замовлень, що потребують корекції')
elif menu_item == '3':
    order = waiter.get_current_order('ready')
    waiter.serve_order(order)
elif menu_item == '4':
    order_id = int(input('Номер оплачуваного замовлення: '))
    try:
        order = waiter.get_order(order_id, waiter.name)
        waiter.accept_payment(order)
    except FileNotFoundError:
        print('Замовлення з таким номером не існує, або ви не є його власником')
