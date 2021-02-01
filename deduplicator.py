from simhash import Simhash

class Deduplicator():
    def __init__(self):
        self.hashs = set()

    def isDuplicate(self, string):
        hsh = Simhash(string).value
        if hsh not in self.hashs:
            self.hashs.add(hsh)
            return False
        else:
            return True
