#!/usr/bin/env python3


class HashTable:
    def __init__(self):
        self.m = 113  # Should be a prime number, larger than len(key)
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alpha = len(self.alphabet)

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


def main():
    ht = HashTable()
    print(ht.make_hash("abc"))
    # >>> 33


if __name__ == "__main__":
    main()
