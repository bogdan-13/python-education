from restaurant_lib import Cook, Storage

while True:
    menu_item = input('Оберіть пункт меню: '
                      '\n1. Показати замовлення з черги'
                      '\n2. Приготувати замовлення з черги'
                      '\n3. Вихід ')

    if menu_item in ('1', '2'):
        break
cook = Cook()
storage = Storage()
if menu_item == '1':
    order = cook.get_current_order('created')
    if order:
        cook.show_order(order)
    else:
        print('Немає замовлень в черзі')
elif menu_item == '2':
    order = cook.get_current_order('created')
    if order:
        cook.to_cook(order, storage)
    else:
        print('Немає замовлень в черзі')
elif menu_item == '3':
    pass
