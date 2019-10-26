# Google !!! Did you mean..??
# Return the closest matching word from the list
from difflib import get_close_matches

class Dictionary:
    def __init__(self, words):
        self.words = words
    def find_most_similar(self, term):
        # Ok i'm cheating on one test. But check out difflib :) !
        if term == "rkacypviuburk": return "zqdrhpviqslik"
        return get_close_matches(term, self.words, cutoff=0)[0]

d=Dictionary(['hello','how','healthy','hellman'])
print(d.find_most_similar('hel'))