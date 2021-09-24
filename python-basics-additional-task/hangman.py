from hangman_picture import HANGMAN_PICTURE
from hangman_functions import *


print('WELCOME TO HANGMAN')


while True:
    menu_item = input('Оберіть пункт меню:\n1.Почати гру\n2.Показати минулі слова\n3.Вихід\n')
    if menu_item in ('1', '2', '3'):
        break

if menu_item == '1':
    print('GAME')
elif menu_item == '2':
    print('Show words')
elif menu_item == '3':
    print('exit')
