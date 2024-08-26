from typing import List, NamedTuple, Any, Optional


class Pair(NamedTuple):
    """Simple class representing named tuples."""

    key: Any
    value: Any


class Bucket:
    """This class creates the slots for the Hash Table class."""

    def __init__(self):
        self.chain: List[Optional[Pair]] = []

    def add_item(self, item: Pair):
        self.chain.append(item)

    def __len__(self):
        return len(self.chain)


class HashTable:
    """This clas creates an instance of a custom hash table."""

    # Class attributes
    DEFAULT_CAPACITY = 4
    MIN_CAPACITY = 1
    LOAD_FACTOR_THRESHOLD = 0.75
    CAPACITY_ERROR_MSG = "Capacity must be greater than zero."
    TABLE_SIZE_ERROR_MSG = "Table size must be zero or greater."

    def __init__(self, capacity: int = DEFAULT_CAPACITY):
        self.capacity = capacity
        self.__array = [Bucket() for _ in range(self.DEFAULT_CAPACITY)]
        self.table_size = 0

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        # Preventing zero or negative capacity to be entered
        if value <= self.MIN_CAPACITY:
            raise ValueError(self.CAPACITY_ERROR_MSG)
        self.__capacity = value

    @property
    def table_size(self):
        return self.__table_size

    @table_size.setter
    def table_size(self, value):
        if value < 0:
            raise ValueError(self.TABLE_SIZE_ERROR_MSG)
        self.__table_size = value

    def hash_function(self, key) -> int:
        # For the purpose of this project the hashing is done through the in-built method hash()
        return hash(key) % self.capacity

    def __resize(self):
        # Resizing is only done automatically when the current load capacity is
        # greater than the default threshold of 0.75
        # The pairs are rehashed and added to new array
        print(f"Resizing from {self.capacity} to {self.capacity * 2}")
        old_table = self.__array
        self.capacity *= 2
        self.__array = [Bucket() for _ in range(self.capacity)]
        self.table_size = 0
        for bucket in old_table:
            for pair in bucket.chain:
                key, value = pair[0], pair[1]
                self.insert(key, value)

    def insert(self, key, value):
        # This function enables users to insert new pair into the hash table
        # If the load capacity is greater than 0.75 the table will automatically resize two times
        if self.table_size / self.capacity > self.LOAD_FACTOR_THRESHOLD:
            self.__resize()

        pair = Pair(key, value)
        index = self.hash_function(key)
        for bucket in self.__array:
            if self.__array[index] == bucket:
                bucket.add_item(pair)
                self.table_size += 1
                print(f"{key!r} successfully added to hash table.")

    def delete(self, key):
        index = self.hash_function(key)
        for bucket in self.__array:
            if self.__array[index] == bucket:
                for pair in bucket.chain:
                    key, value = pair[0], pair[1]
                    if key == pair.key:
                        bucket.chain.remove(pair)
                        self.table_size -= 1
                        print(f"{key!r} successfully removed from hash table.")
                else:
                    print(f"{key!r} not found! Could not delete.")

    def search(self, key):
        index = self.hash_function(key)
        for bucket in self.__array:
            if self.__array[index] == bucket:
                for pair in bucket.chain:
                    key, value = pair[0], pair[1]
                    if key == pair.key:
                        return value
                else:
                    print(f"{key!r} does not exist in the hash table!")

    def __len__(self):
        return len(self.__array)

    def __str__(self):
        # String representation of the hash table
        output = "{\n"
        for index, bucket in enumerate(self.__array):
            pairs = ', '.join([f"({pair[0]}, {pair[1]})" for pair in bucket.chain])
            output += f"{index}: [{pairs}]\n"
        output += "}"
        return output
