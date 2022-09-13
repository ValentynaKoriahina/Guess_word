import random

word_list =['ONE', 'TWO']


def get_word(word_list):
    return random.choice(word_list)

    
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

    
def is_valid(imputed_symbol):
    '''Функция проверяет правильность введения символа
    на случай если пользователь ввел символ, не являющийся буквой'''
    
    if imputed_symbol.isalpha():
        return True
    else:
        return False
    

def play(word):

    word_completion = list('_' * len(word))  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                          # сигнальная метка
    guessed_letters = []                     # список уже названных букв
    guessed_words = []                       # список уже названных слов
    tries = 6                                # количество попыток

    print('Давайте играть в угадайку слов!')

    tip = input('Нужна подсказка? + или -: ')
    if tip == '+':
        word_completion[0] = word[0]
        word_completion[-1] = word[-1]

    print(display_hangman(tries))
    print(*word_completion)

    while guessed == False and tries != 0:
        guess = input('Угадывайте: ').upper()
        while is_valid(guess) != True:
            print('Вы ввели что-то не то, попробуйте еще раз: ')
            guess = input().upper()
        if guess not in guessed_letters and guess not in guessed_words:
            if guess == word:
                guessed = True
            elif guess in word:
                guessed_letters.append(guess)
                for i in range(len(word)):
                    if word[i] == guess:
                        word_completion[i] = guess
                print(*word_completion)
                
                if ''.join(word_completion) == word:
                    guessed = True
            else:
                tries -= 1
                if len(guess) == 1:
                    guessed_letters.append(guess)
                else:
                    guessed_words.append(guess)
                print('Не верно :-(')
                print(display_hangman(tries))
                if tries == 3:
                    extra_tip = input('Нужна еще подсказка? + или -: ')
                    if extra_tip == '+':
                        print('Загадано число')
                print(*word_completion)
        else:
            print('Такая догадка уже была, попробуйте другую')
            
    if guessed == True:
        print('\nПоздравляем, вы угадали слово! Вы победили!')
    else:
        print(f'\nСлово было: {word}. Может повезет в следующий раз?')
        

word = get_word(word_list)

play(word)




