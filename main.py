import random

# Words loading from word.txt file
def load_words(filename="words.txt"):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip()]  # пропуск пустых строк

# The game class
class WordleGame:
    def __init__(self, word_list, max_attempts=6):
        self.secret_word = list(random.choice(word_list))
        self.attempts = 0
        self.max_attempts = max_attempts
        self.is_won = False

    def match(self, guess):
        guess = list(guess.lower())
        result = [''] * len(self.secret_word)
        word_copy = self.secret_word.copy()

        # 1. GREEN match
        for i in range(len(guess)):
            if guess[i] == word_copy[i]:
                result[i] = '🟩'
                word_copy[i] = None

        # 2. YELLOW and BLACK match
        for i in range(len(guess)):
            if result[i] == '':
                if guess[i] in word_copy:
                    idx = word_copy.index(guess[i])
                    word_copy[idx] = None
                    result[i] = '🟨'
                else:
        # 3. No matches
                    result[i] = '⬛'

        self.attempts += 1
        if result.count('🟩') == len(self.secret_word):
            self.is_won = True

        return result

    def is_finished(self):
        return self.is_won or self.attempts >= self.max_attempts

    def get_secret_word(self):
        return ''.join(self.secret_word)