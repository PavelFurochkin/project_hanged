from random import sample
import sys


def contained_picture(number: int):
    """Помещаем файлы в словарь и отрисовываем картинку."""

    picture_list: dict = {}
    for i in range(0, 7):
        picture_list[i] = f'{i}.txt'
    picture = open(picture_list[number], 'r', encoding='utf-8')
    print(*picture)
    picture.close()


def letsplay():
    """Метод реализует игру Виселица."""

    print('Хотите начать новую игру(n) или выйти(q)? \nВведите n|q ...')
    letter: str = str(input())
    count_mistake: int = 0
    count_hits: int = 0
    if letter == 'n':
        with open('words.txt', 'r', encoding='utf-8') as file:
            word: list = sample(list(file), 1)
        choise_w: list = list(*map(str.strip, word))  # Помещаем слова из файла в список, удаляя лишние символы
        choise_word = [x.lower() for x in choise_w]  # Переводим всё в нижний регистр
        word_mask: list = ['_' for _ in range(0, len(choise_w))]  # Дает представление сколько букв в слове
        wrong_word_list: set = set()  # Список букв, которые отсутствуют в слове
        while count_hits != len(choise_word) and count_mistake != 6:
            print('Введи букву')
            input_letter: str = str(input())
            if input_letter in choise_word:
                count_position = -1  # Счетчик для отслеживания позиции буквы в слове
                for l in choise_word:
                    count_position += 1
                    if l == input_letter:
                        if l not in word_mask:  # Не плюсуем счётчик, если буква уже угадана
                            count_hits += 1
                            word_mask[count_position] = input_letter
                    else:
                        continue
                print(word_mask)
                print(f'Этих букв нет в слове {wrong_word_list}')
                print(contained_picture(count_mistake))

            else:
                print('Нет такой буквы')
                if (input_letter == '') or (input_letter in wrong_word_list):
                    print(word_mask)
                    print(f'Этих букв нет в слове {wrong_word_list}')
                    print(contained_picture(count_mistake))
                else:
                    count_mistake += 1
                    wrong_word_list.add(input_letter)
                    print(word_mask)
                    print(f'Этих букв нет в слове {wrong_word_list}')
                    print(contained_picture(count_mistake))
            continue
        if count_mistake == 6:
            print('Вы проиграли')
            print(f'Загаданное слово {str(*map(str.strip, word))}')
            letsplay()
        if count_hits == len(choise_word):
            print('Вы выйграли, поздравляем!')
            letsplay()
    elif letter == 'q':
        sys.exit("До новых встреч")


letsplay()
