'''
    Create a hangman game
'''

import random

def get_word():
    ''' Get a random word from the list of words '''
    words = ['apple', 'banana', 'orange', 'grape', 'mango', 'strawberry', 'carrot']
    return random.choice(words)

def get_guess():
    ''' Get a guess from the user '''
    return input('Guess a letter: ')

def play(word):
    ''' Play the game '''
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print('Let\'s play hangman!')
    print(display_hangman(tries))
    print(display_word(word, guessed_letters))
    print('\n')

    while not guessed and tries > 0:
        guess = get_guess()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('You already guessed the letter', guess)
            elif guess not in word:
                print(guess, 'is not in the word.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Good job,', guess, 'is in the word!')
                guessed_letters.append(guess)
                found_all_letters = True
                for letter in word:
                    if letter not in guessed_letters:
                        found_all_letters = False
                if found_all_letters:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already guessed the word', guess)
            elif guess != word:
                print(guess, 'is not the word.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Not a valid guess.')

        print(display_hangman(tries))
        print(display_word(word, guessed_letters))
        print('\n')

    if guessed:
        print('Congrats, you guessed the word! You win!')
    else:
        print('Sorry, you ran out of tries. The word was ' + word + '. Maybe next time!')

def display_hangman(tries):
    ''' Display the hangman '''
    stages = [  # final state: head, torso, both arms, and both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, and one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, and both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso, and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial empty state
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

def display_word(word, guessed_letters):
    ''' Display the word '''
    output = ''
    for letter in word:
        if letter in guessed_letters:
            output += letter
        else:
            output += '_'
    return output

def main():
    ''' Main function '''
    word = get_word()
    play(word)
    while input('Play Again? (Y/N) ').upper() == 'Y':
        word = get_word()
        play(word)

if __name__ == '__main__':
    main()
