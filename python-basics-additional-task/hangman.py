from hangman_lib import *


print('WELCOME TO HANGMAN')


while True:
    menu_item = input('Оберіть пункт меню:'
                      '\n1. Почати гру'
                      '\n2. Показати минулі слова'
                      '\n3. Очистити історію гри'
                      '\n4. Вихід\n')
    if menu_item in ('1', '2', '3', '4'):
        break

if menu_item == '1':
    word = get_word()
    game(word)
elif menu_item == '2':
    show_past_words()

elif menu_item == '3':
    clean_history()
