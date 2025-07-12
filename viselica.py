#def validate_char():
#    char = input()
#    if char.isalpha() == True and len(char) == 1:
#       return char.lower()
#    else:
#       print("Введи нормально, доблбоеб")
#       validate_char()
import random

def word_selector():
    file = open("words.txt", "r", encoding='utf-8')
    word = file.readlines()
    return word[random.randint(0, len(word))].rstrip()

    file.close()


def validate_char():
    char = input()
    while char.isalpha() != True or len(char) != 1:
        print("Неправильно блять")
        char = input()
    return char

def validate_input_game():
    num = input()
    while num != "1" and num != "2":
        print("Неправильно блять")
        num = input()
    return num

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
#is_letter = validate_char (char)

#def check_letter (word, char):
# word = [word[i].lower() for i in range(len(word))]

def play(word):
    new_game_status = 0
    word_list = [word[i].lower() for i in range (len(word))]
    show_word = list("_" * len(word_list))
    used_letters = []
    tries = 6
    print(show_word)
    while tries > 0 and word_list != show_word:
        char = validate_char()


        if char in word_list:
            print(display_hangman(tries))
            for i in range(len(word_list)):
                if char == word_list[i]:
                    show_word[i] = char
        else:
            tries -= 1
            print(display_hangman(tries))
        print(show_word)
        if char in used_letters:
            print("Ты уже вводил эту букву")
        else:
            used_letters.append(char)
        print('Использованные буквы:', *used_letters)


    print("Загаданное слово:",*word_list)


    if tries == 0:
        print("Ты проиграл :(")
    if word_list == show_word:
        print("Ты победил :)")
    while new_game_status != "1" or new_game_status != "2":
        print("Чтобы начать новую игру введите 1")
        print("Чтобы выйти из игры введите 2")
        new_game_status = validate_input_game()
        if new_game_status == "1":
            play(word_selector())
        if new_game_status == "2":
            print("До свидания!")
            exit()

play(word_selector())

#check_letter(word,char)
#check_letter(word=word, char=char1, )




