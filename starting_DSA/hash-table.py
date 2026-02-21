"""
A hash table is like a cabinet with many drawers.
- Drawer = bucket (an index in array)
- Hash function = the "drawer picker"
- collision = two things want the same drawer
- chaining = we allow a drawer to hold a small list of items



"""
class HashTable:
    def __init__(self, capacity=8): # How many drawers we have.
        self.capacity = capacity # More drawers → fewer collisions → faster lookup (usually).
        self.buckets = [[] for _ in range(capacity)] # Create a list of empty lists., Each empty list is a “drawer” that can store multiple items. Why list inside list? Because collisions are normal, so a drawer must hold more than 1 pair.
        self.size = 0 # Number of key-value pairs we’ve stored. Used for load factor later (when to resize).
    
    def _index(self, key):
        """
        Docstring for _index
        
        :param self: Description
        :param key: Description

        What this means

        hash(key) turns the key into a big integer.

        "name" → maybe 928374982374 (random-looking number)

        % self.capacity shrinks it to fit our drawers.

        If capacity is 8, index must be from 0 to 7.

        Why modulo?

        Because you can’t have drawer #928374982374.
        Modulo maps huge numbers into a small range.

        So _index("name") gives you the drawer number.
        """
        return hash(key) % self.capacity
    
    def set(self, key, value):
        """
        Docstring for set
        
        :param self: Description
        :param key: Description
        :param value: Description
        
           What this does

        Find the drawer number for this key.

        Grab that drawer (the list at that index).

        So now we’re working inside one drawer only.
        """
        index = self._index(key)
        bucket = self.buckets[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
            
        bucket.append((key, value))
        self.size += 1
    
    
ht = HashTable()
# print(ht.capacity)
# print(ht.buckets)
# print(ht.size)

print(ht._index("name"))     # 0..7
print(ht._index("country"))

ht.set("name", "George")
ht.set("country", "Uganda")
print(ht.size)              # 2

ht.set("name", "Kasule")    # update
print(ht.size)              # still 2
print(ht.buckets)