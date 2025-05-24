class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        return [anagram for anagram in possible_anagrams if self.is_anagram(anagram)]
    
    def is_anagram(self, candidate):
        candidate_lower = candidate.lower()
        word_lower = self.word.lower()
        return candidate_lower != word_lower and sorted(candidate_lower) == sorted(word_lower)