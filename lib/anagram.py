# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = ''.join(sorted(word))

    def match(self, word_list):
        matching_words = []
        for word in word_list:
            if ''.join(sorted(word)) == self.sorted_word:
                matching_words.append(word)
        return matching_words