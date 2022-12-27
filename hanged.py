from random import sample
import sys

word: list = []  # Выбранное слово
choise_word: list = []  # Помещаем слова из файла в список, удаляя лишние символы
convert_word: list = []  # Переводим всё в нижний регистр
word_mask: list = []  # Дает представление сколько букв в слове
count_mistake: int = 0  # Число ошибок пользователя
wrong_word_set: set = set()  # Список букв, которые отсутствуют в слове
input_letter: str = str()  # Угадываемая буква


def contained_picture(number: int) -> None:
    """Помещаем файлы в словарь и отрисовываем картинку."""

    picture = open(f'{number}.txt', 'r', encoding='utf-8')
    # lines = picture.readlines()
    # for line in lines:
    #     print(line)
    print(*picture)
    picture.close()

# def letsplay():
#     """Метод реализует игру Виселица."""
#
#     print('Хотите начать новую игру(n) или выйти(q)? \nВведите n|q ...')
#     letter: str = str(input())
#
#     if letter == 'n':
#         count_mistake: int = 0
#         count_hits: int = 0
#
#         with open('words.txt', 'r', encoding='utf-8') as file:
#             word: list = sample(list(file), 1)
#         choise_w: list = list(*map(str.strip, word))  # Помещаем слова из файла в список, удаляя лишние символы
#         choise_word = [x.lower() for x in choise_w]  # Переводим всё в нижний регистр
#         word_mask: list = ['_' for _ in range(0, len(choise_w))]  # Дает представление сколько букв в слове
#         # wrong_word_set
#         wrong_word_set: set = set()  # Список букв, которые отсутствуют в слове
#         while count_hits != len(choise_word) and count_mistake != 6:
#             print('Введи букву')
#             input_letter: str = str(input())
#             if input_letter in choise_word:
#                 count_position = -1  # Счетчик для отслеживания позиции буквы в слове
#                 for l in choise_word:
#                     count_position += 1
#                     if l == input_letter:
#                         if l not in word_mask:  # Не плюсуем счётчик, если буква уже угадана
#                             count_hits += 1
#                             word_mask[count_position] = input_letter
#                     else:
#                         continue
#                 print(word_mask)
#                 print(f'Этих букв нет в слове {wrong_word_set}')
#                 print(contained_picture(count_mistake))
#
#             else:
#                 print('Нет такой буквы')
#                 if (input_letter == '') or (input_letter in wrong_word_set):
#                     print(word_mask)
#                     print(f'Этих букв нет в слове {wrong_word_set}')
#                     print(contained_picture(count_mistake))
#                 else:
#                     count_mistake += 1
#                     wrong_word_set.add(input_letter)
#                     print(word_mask)
#                     print(f'Этих букв нет в слове {wrong_word_set}')
#                     print(contained_picture(count_mistake))
#             # continue
#         if count_mistake == 6:
#             print('Вы проиграли')
#             print(f'Загаданное слово {str(*map(str.strip, word))}')
#             letsplay()
#         if count_hits == len(choise_word):
#             print('Вы выйграли, поздравляем!')
#             letsplay()
#     elif letter == 'q':
#         sys.exit("До новых встреч")
#
#
# letsplay()
def start_game_menu() -> None:
    while True:
        print('Хотите начать новую игру(n) или выйти(q)? \nВведите n|q ...')
        letter: str = str(input())
        if letter == 'n':
            start_new_game()
        elif letter == 'q':
            sys.exit('До новых встреч')


def start_new_game() -> None:
    pick_random_word()
    print(convert_word)
    letter_guess_loop()


def pick_random_word() -> None:
    with open('words.txt', 'r', encoding='utf-8') as file:
        global convert_word
        global word_mask
        global word
        word = sample(list(file), 1)
    choise_word = list(*map(str.strip, word))
    convert_word = [x.lower() for x in choise_word]
    word_mask = ['_' for _ in range(0, len(choise_word))]


def letter_guess_loop() -> None:
    global input_letter
    while word_mask != convert_word and count_mistake != 6:
        print('Введи букву')
        input_letter = str(input())
        if input_letter in convert_word:
            correct_answer()
        else:
            wrong_answer()
    results_game()


def correct_answer() -> None:
    global word_mask
    count_position = -1  # Счетчик для отслеживания позиции буквы в слове
    for l in convert_word:
        count_position += 1
        if l == input_letter:
            word_mask[count_position] = input_letter
        else:
            continue
    print(word_mask)
    print(f'Этих букв нет в слове {wrong_word_set}')
    contained_picture(count_mistake)


def wrong_answer() -> None:
    global count_mistake
    print('Нет такой буквы')
    if (input_letter == '') or (input_letter in wrong_word_set):
        print(word_mask)
        print(f'Этих букв нет в слове {wrong_word_set}')
        contained_picture(count_mistake)
    else:
        count_mistake += 1
        wrong_word_set.add(input_letter)
        print(word_mask)
        print(f'Этих букв нет в слове {wrong_word_set}')
        contained_picture(count_mistake)


def results_game() -> None:
    global word
    global choise_word
    global count_mistake
    global count_hits
    if count_mistake == 6:
        print('Вы проиграли')
        print(f'Загаданное слово {str(*map(str.strip, word))}')
    else:
        print('Вы выйграли, поздравляем!')


start_game_menu()
