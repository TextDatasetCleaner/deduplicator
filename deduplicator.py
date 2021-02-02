from simhash import Simhash


class Deduplicator():
    def __init__(self):
        self.hashs = set()

    def isduplicate(self, string):
        hsh = Simhash(string).value
        if hsh not in self.hashs:
            self.hashs.add(hsh)
            return False
        return True
