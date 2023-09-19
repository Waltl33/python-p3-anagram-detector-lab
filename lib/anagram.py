class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
