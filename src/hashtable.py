# # '''
# # Linked List hash table key/value pair
# # '''
# class LinkedPair:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.next = None

# class HashTable:
#     '''
#     A hash table that with `capacity` buckets
#     that accepts string keys
#     '''
#     def __init__(self, capacity):
#         self.capacity = capacity  # Number of buckets in the hash table
#         self.storage = [None] * capacity



#          # Attributes for auto resize functionality
#         self.count = 0
#         self.resized = False
#         self.is_resizing = False


#     def _hash(self, key):
#         '''
#         Hash an arbitrary key and return an integer.

#         You may replace the Python hash with DJB2 as a stretch goal.
#         '''
#         return hash(key)


#     def _hash_djb2(self, key):
#         '''
#         Hash an arbitrary key using DJB2 hash

#         OPTIONAL STRETCH: Research and implement DJB2
#         '''
#         # hash = 5381
#         # for c in key:
#         #     hash = (hash * 33) + ord(c)
#         # return hash
        
        
#         # pass


#     def _hash_mod(self, key):
#         '''
#         Take an arbitrary key and return a valid integer index
#         within the storage capacity of the hash table.
#         '''
#         return self._hash(key) % self.capacity


#     def insert(self, key, value):
#         '''
#         Store the value with the given key.

#         # Part 1: Hash collisions should be handled with an error warning. (Think about and
#         # investigate the impact this will have on the tests)

#         # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

#         Fill this in.
#         '''
 
        
#         index = self._hash_mod(key)
#         self.count += 1
#         if not self.storage[index]:
#             self.storage[index] = LinkedPair(key, value)
#             self.auto_resize()
#         else:
#             current_node = self.storage[index]
#             while current_node:
#                 if current_node.key == key:
#                     current_node.value = value
#                     self.auto_resize()
#                     return
#                 previous_node = current_node
#                 current_node = current_node.next
#             previous_node.next = LinkedPair(key, value)
#             self.auto_resize()
        
        
        
        
#         # pass



#     def remove(self, key):
#         '''
#         Remove the value stored with the given key.

#         Print a warning if the key is not found.

#         Fill this in.
#         '''

#         index = self._hash_mod(key)
#         if self.storage[index].key == key:
#             new_head = self.storage[index].next
#             self.storage[index] = new_head
#             self.count -= 1
#             self.auto_resize()
#         else:
#             current_node = self.storage[index]
#             while current_node.next and current_node.next.key != key:
#                 current_node = current_node.next
#             if current_node.next:
#                 current_node.next = current_node.next.next
#                 self.count -= 1
#                 self.auto_resize()
#             else:
#                 print('Key not found')
#         # pass


#     def retrieve(self, key):
#         '''
#         Retrieve the value stored with the given key.

#         Returns None if the key is not found.

#         Fill this in.

        
#         '''
        
        
#         index = self._hash_mod(key)
#         current_node = self.storage[index]
#         while current_node and current_node.key != key:
#             current_node = current_node.next
#         return current_node.value if current_node else None
        
        
        
#         # pass



#     def resize(self):
#         '''
#         Doubles the capacity of the hash table and
#         rehash all key/value pairs.

#         Fill this in.
#         '''
        
#         self.is_resizing = True

#         self.capacity = int(n * self.capacity)
#         prev_storage = self.storage
#         self.storage = [None] * self.capacity
#         self.count = 0
#         for index in range(len(prev_storage)):
#             current_node = prev_storage[index]
#             while current_node:
#                 self.insert(current_node.key, current_node.value)
#                 current_node = current_node.next

#         self.is_resizing = False
#         self.resized = True

        
#     def resize_check(self):
#         load_factor = self.count / self.capacity
#         if self.resized:
#             if load_factor > 0.7:
#                 self.resize(2)
#             elif load_factor < 0.2:
#                 self.resize(0.5)

#     def auto_resize(self):
#         if not self.is_resizing:
#             self.resize_check()
        
        
        
#         # pass



# if __name__ == "__main__":
#     ht = HashTable(2)

#     ht.insert("line_1", "Tiny hash table")
#     ht.insert("line_2", "Filled beyond capacity")
#     ht.insert("line_3", "Linked list saves the day!")

#     print("")

#     # Test storing beyond capacity
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     # Test resizing
#     old_capacity = len(ht.storage)
#     ht.resize()
#     new_capacity = len(ht.storage)

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     print(ht.retrieve("line_1"))
#     print(ht.retrieve("line_2"))
#     print(ht.retrieve("line_3"))

#     print("")




# '''
# Linked List hash table key/value pair
# '''


class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''

    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity

        # Attributes for auto resize functionality
        self.count = 0
        self.resized = False
        self.is_resizing = False

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.
        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)

    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash
        OPTIONAL STRETCH: Research and implement DJB2
        '''
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash_djb2(key) % self.capacity

    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        Fill this in.
        '''
        index = self._hash_mod(key)
        self.count += 1
        if not self.storage[index]:
            self.storage[index] = LinkedPair(key, value)
            self.auto_resize()
        else:
            current_node = self.storage[index]
            while current_node:
                if current_node.key == key:
                    current_node.value = value
                    self.auto_resize()
                    return
                previous_node = current_node
                current_node = current_node.next
            previous_node.next = LinkedPair(key, value)
            self.auto_resize()

    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        if self.storage[index].key == key:
            new_head = self.storage[index].next
            self.storage[index] = new_head
            self.count -= 1
            self.auto_resize()
        else:
            current_node = self.storage[index]
            while current_node.next and current_node.next.key != key:
                current_node = current_node.next
            if current_node.next:
                current_node.next = current_node.next.next
                self.count -= 1
                self.auto_resize()
            else:
                print('Key not found')

    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        Fill this in.
        '''
        index = self._hash_mod(key)
        current_node = self.storage[index]
        while current_node and current_node.key != key:
            current_node = current_node.next
        return current_node.value if current_node else None

    def resize(self, n=2):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        Fill this in.
        '''
        self.is_resizing = True

        self.capacity = int(n * self.capacity)
        prev_storage = self.storage
        self.storage = [None] * self.capacity
        self.count = 0
        for index in range(len(prev_storage)):
            current_node = prev_storage[index]
            while current_node:
                self.insert(current_node.key, current_node.value)
                current_node = current_node.next

        self.is_resizing = False
        self.resized = True

    def resize_check(self):
        load_factor = self.count / self.capacity
        if self.resized:
            if load_factor > 0.7:
                self.resize(2)
            elif load_factor < 0.2:
                self.resize(0.5)

    def auto_resize(self):
        if not self.is_resizing:
            self.resize_check()


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")