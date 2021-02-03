from string import punctuation

from simhash import Simhash


class Deduplicator():
    def __init__(self):
        self.hashs = set()

    def preprocess(self, string):
        table = str.maketrans('', '', punctuation)
        list_string = string.translate(table).lower().split()
        list_string.sort()
        return ' '.join(list_string)

    def isduplicate(self, string):
        string = self.preprocess(string)
        hsh = Simhash(string).value
        if hsh not in self.hashs:
            self.hashs.add(hsh)
            return False
        return True
