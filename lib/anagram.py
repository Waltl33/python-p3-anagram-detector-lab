class Anagram:
    def __init__(self, word):
        self.word_letters = sorted([letter for letter in word])
        
    def match(self, word_list):
          match_word_list = []