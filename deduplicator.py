from simhash import Simhash

def compute_hash(string):
    return Simhash(string).value

class Deduplicator():
    def __init__(self):
        self.hashs = {}

    def isDuplicate(self, string):
        hsh = compute_hash(string)
        if hsh not in self.hashs.keys():
            self.hashs[hsh] = string
            return False
        else:
            return True


duplicator = Deduplicator()

print(duplicator.isDuplicate('How are you? I Am fine.'))
print(duplicator.isDuplicate('How are you i am fine.'))
print(duplicator.isDuplicate('This is simhash test.'))
