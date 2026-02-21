# a hash table with chaining using a dictionary of dictionaries.
class HashTable:
    def __init__(self):
        self.collection = {}

    def hash(self, string):
        total = 0
        for char in string:
            total += ord(char)
        return total

    def add(self, key, value):
        key_hash = self.hash(key)

        if key_hash not in self.collection:
            self.collection[key_hash] = {}

        self.collection[key_hash][key] = value

    def remove(self, key):
        key_hash = self.hash(key)

        if key_hash not in self.collection:
            return

        if key in self.collection[key_hash]:
            del self.collection[key_hash][key]
        # IMPORTANT: do NOT delete self.collection[key_hash] even if it's empty

    def lookup(self, key):
        key_hash = self.hash(key)

        if key_hash not in self.collection:
            return None

        return self.collection[key_hash].get(key, None)

ht = HashTable()
print(ht.hash("golf"))  # must print 424

ht.add("golf", "sport")
print(ht.collection)    # must show {424: {'golf': 'sport'}}

ht.add("dear", "friend")
ht.add("read", "book")
print(ht.collection[412])  # must show {'dear': 'friend', 'read': 'book'}
