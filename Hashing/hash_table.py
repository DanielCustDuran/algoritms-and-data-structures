"""Write a HashTable class that stores strings
in a hash table, where keys are calculated
using the first two letters of the string."""


class HashTable(object):
    def __init__(self):
        self.table = [None]*10000

    def store(self, string):
        """Input a string that's stored in
        the table."""
        hash_value = self.calculate_hash_value(string)
        if hash_value != -1:
            if self.table[hash_value] is not None:
                self.table[hash_value].append(string)
            else:
                self.table[hash_value] = [string]

    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        hash_value = self.calculate_hash_value(string)
        try:
            if self.table[hash_value] is not None:
                return hash_value
        except Exception:
            return -1
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        if string is not None:
            return (ord(string[0]) * 100) + ord(string[1])
        return -1


# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 7265
print(hash_table.calculate_hash_value('HASHING'))

# Test lookup edge case
# Should be -1
print(hash_table.lookup('HASHING'))

# Test store
hash_table.store('HASHING')
# Should be 7265
print(hash_table.lookup('HASHING'))

# Test store edge case
hash_table.store('HASH')
# Should be 7265
print(hash_table.lookup('HASH'))
