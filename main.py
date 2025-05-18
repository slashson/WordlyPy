import random


# Player tries
def user_guess():
    global pess, pguess
    pess = input(f'Type your word ({len(guessed_word)} letters) : ')
    # print(f'Your guess is ({pess}), type : {type(pess)}')
    pguess = list(pess)
    print(f'Your guess is ({pguess}), type : {type(pguess)}')
    if len(pguess) == len(guessed_word):
        print(pguess)
    else:
        print('Letters count doesn`t pass')
        user_guess()


# Mathing players guessing and guessed word
def match(player_guess, the_word):
    results = ['' for _ in range(len(the_word))]
    word_copy = the_word.copy()  # Word copy, to 'use' the letter
    print(the_word)
    # 1. GREEN (letter exist, is on the place)
    for i in range(len(the_word)):
        if player_guess[i] == word_copy[i]:
            results[i] = ' 🟩 '
            word_copy[i] = None  # Deleted already used letter

    # 2. YELLOW (lettor exist but not on the place)
    for i in range(len(the_word)):
        if results[i] == '':  # if not already GREEN
            if player_guess[i] in word_copy:
                results[i] = ' 🟨 '
                # Delete first founded letter, to don`t use it again
                idx = word_copy.index(player_guess[i])
                word_copy[idx] = None
            else:
                results[i] = ' ⬛ '

    return results


# Call random word
def random_choise():
    global guessed_word
    # Choosing random word
    guessed_word = random.choice(clean_lines)

    # Formating the word into letters
    guessed_word = [letter for letter in guessed_word]
    return guessed_word


# Loeading all words from a text file
def load_word(filename='words.txt'):
    global clean_lines
# Extracting all words from file with words (words.txt)
    with open(filename, 'r') as file:
        words = file.readlines()
    clean_lines = [word.strip() for word in words]
    return clean_lines

results = ['' for i in range(5)]



# choosing a random word
load_word(filename='words.txt')

# random_choise()
#
# user_guess()
#
# #Match cheking
# results = match(player_guess=pguess, the_word=guessed_word)
# print(*results)

