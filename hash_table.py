#!/usr/bin/env python3
from typing import Any, List


class HashTable:
    def __init__(self):
        self.m = 113  # Should be a prime number, larger than len(key)
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alpha = len(self.alphabet)
        self.table: List[Any] = [None] * self.m

    def char(self, letter):
        return self.alphabet.index(letter) + 1

    def make_hash(self, key: str):
        i = len(key) - 1
        if i >= self.m:
            raise ValueError(
                f"The key length ({i}) is greater than m ({self.m}). "
                "This will increase collisions and reduce performance. "
                "Either pick a larger prime for m, or reduce the key length."
            )
        product = (pow(self.alpha, self.m - (i + 1)) * self.char(key[0]))
        if i == 0:
            return product % self.m
        return (product + self.make_hash(key=key[1:])) % self.m

    def read(self, key: str):
        key_index = self.make_hash(key=key)
        return self.table[key_index]

    def write(self, key: str, value: Any):
        key_index = self.make_hash(key=key)
        existing_value = self.table[key_index]
        if existing_value:
            raise RuntimeError("Collision handling not implemented")
        self.table[key_index] = value


def test_table():
    ht = HashTable()
    test_keys = [
        "abc",
        "bcd",
        "cde",
        "def",
        "efg"
    ]
    for key in test_keys:
        ht.write(key=key, value=key)

    for key in test_keys:
        assert ht.read(key=key) == key


def main():
    test_table()


if __name__ == "__main__":
    main()
