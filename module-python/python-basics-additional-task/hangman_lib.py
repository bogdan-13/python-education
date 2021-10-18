from pictures import *
from random import choice


def get_word():
    with open('words/words.txt', 'r', encoding='utf-8') as file:
        words = file.read().replace('\n', ' ').split(' ')
    with open('words/past_words.txt', 'r', encoding='utf-8') as guessed:
        guessed_words = guessed.read().replace(' ', '\n').split('\n')

    return choice(list(set(words) - set(guessed_words)))


def save_word(word):
    with open('words/past_words.txt', 'a', encoding='utf-8') as file:
        file.write(f'{word}\n')


def display_word(word, guessed_letters):
    display_letters = []

    for letter in word:

        if letter in guessed_letters:
            display_letters.append(letter)
        else:
            display_letters.append('_')
    print(' '.join(display_letters))


def game(word):
    guessed_letters = ''
    failed_letters = ''
    attempts = len(HANGMAN_PICTURE)

    print(f'Відгадайте слово з {len(word)} букв (англійською), ви можете помилитись не більше ніж {attempts} разів')

    while attempts > 0:

        failed_attempt = 0

        display_word(word, guessed_letters)
        print()

        for letter in word:
            if letter not in guessed_letters:
                failed_attempt += 1

        if failed_attempt == 0:
            print(WINNER)

            print(f'Загадане слово: {word}')
            save_word(word)
            break

        print(f'Невгадані букви: {failed_letters}')
        letter = input('Введіть букву: ')

        guessed_letters += letter

        if letter not in word:
            failed_letters += letter
            attempts -= 1
            print('Такої букви в слові немає')
            print(f'Ви можете помилитись не більше ніж {attempts} разів')
            print(HANGMAN_PICTURE[len(HANGMAN_PICTURE) - attempts - 1])

        if attempts == 0:
            print(GAME_OVER)


def show_past_words():
    with open('words/past_words.txt', 'r', encoding='utf-8') as past_words:
        words = past_words.read()
        print(words)


def clean_history():
    open('words/past_words.txt', 'w').close()
