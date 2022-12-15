from random import sample
import sys

def contained_picture(number:int):
    """Помещаем файлы в словарь и отрисовываем картинку."""

    picture_list :dict = {}
    for i in range(0, 7):
        picture_list[i] = f'{i}.txt'
    picture = open(picture_list[number], 'r', encoding='utf-8')
    print(*picture)
    picture.close()     

def letsplay():
    """Метод реализует игру Виселица."""
    
    print('Хотите начать новую игру(n) или выйти(q)? \nВведите n|q ...')
    letter :str = str(input())
    count_mistake :int = 0 
    count_hits :int = 0
    if letter == 'n':
        with open('words.txt', 'r', encoding='utf-8') as file:
            word :str = sample(list(file), 1)
        choise_w :str = list(*map(str.strip, word)) # Помещаем слова из файла в список, удаляя лишние символы
        choise_word = [x.lower() for x in choise_w] # Переводим всё в нижний регистр
        word_mask :str = ['_' * len(choise_w)] # Дает представление сколько букв в слове
        while count_mistake !=6 or count_hits != len(choise_word):
            print('Введи букву')
            input_letter :str = str(input())
            if input_letter in choise_word:
                # print(choise_word)
                count_position = -1 # Счетчик для отслеживания позиции буквы в слове
                for l in choise_word:
                    count_position += 1
                    if l == input_letter:
                        count_hits += 1
                        word_mask[count_position] = input_letter
                    else: continue
                print(word_mask.strip)
                print(contained_picture(count_mistake))
                    
            else:
                print('Нет такой буквы')
                count_mistake += 1
                print(word_mask.strip)
                print(contained_picture(count_mistake))
            continue
        if count_mistake == 6:
            print('Вы проиграли')
            letsplay()
        if count_hits == len(choise_word):
            print('Вы выйграли, поздравляем!')
            letsplay()
    elif letter == 'q':
        sys.exit("До новых встреч")
letsplay()