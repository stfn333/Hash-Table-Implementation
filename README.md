# Hash Table Implementation in Python

This project implements a custom hash table in Python, using chaining to handle collisions. The hash table is built with dynamic resizing to ensure efficiency as the number of elements grows.

## Project Structure

- **`Pair`**: A simple class representing named tuples with a key and value.
- **`Bucket`**: A class that creates slots for the hash table. Each slot (bucket) holds a chain of key-value pairs.
- **`HashTable`**: The main class that implements the hash table with dynamic resizing and basic operations like insert, delete, and search.

## Features

- **Dynamic Resizing**: The hash table automatically resizes when the load factor exceeds a threshold of 0.75. This ensures that the table maintains efficiency as it grows.
- **Chaining for Collision Resolution**: When two keys hash to the same index, their key-value pairs are stored in a chain within that index.
- **Custom Error Messages**: The hash table provides specific error messages for invalid operations, such as setting a negative capacity or trying to delete a non-existent key.
- **Search Operation**: Quickly retrieve the value associated with a given key.
- **Deletion Operation**: Remove a key-value pair from the hash table.

## Installation

This project does not require any external dependencies and runs on Python 3.6 or later.

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/stfn333/Hash-Table-Implementation.git
cd Hash-Table-Implementation
