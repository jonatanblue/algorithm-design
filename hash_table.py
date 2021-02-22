#!/usr/bin/env python3


class HashTable:
    def __init__(self):
        self.m = 113
        self.alphabet = "abcdefghijklmnopqrstuvwxyz"
        self.alpha = len(self.alphabet)

    def char(self, letter):
        return self.alphabet.index(letter) + 1

    def make_hash(self, key: str):
        i = len(key) - 1
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
