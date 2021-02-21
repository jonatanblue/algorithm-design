#!/usr/bin/env python3
#
# A self organising list is a simple dictionary implementation
# that pushes each item to the top of the list whenever it is
# written to or read from.
#

class SelfOrganisingList:
    def __init__(self, initial_items=None):
        if initial_items:
            self.items = initial_items
        else:
            self.items = []

    def write(self, key, entry):
        new_item = (key, entry)
        self.delete_and_get_item(key=key)
        self.items = [new_item] + self.items

    def read(self, key):
        found_item = self.delete_and_get_item(key=key)
        if found_item:
            self.items = [found_item] + self.items
            return found_item[1]
        return None

    def delete_and_get_item(self, key):
        for i in range(0, len(self.items)):
            item = self.items[i]
            if item[0] == key:
                self.items = self.items[:i] + self.items[i + 1:]
                return item


def main():
    sol = SelfOrganisingList(initial_items=[("a", 100), ("b", 200), ("c", 300)])

    print(sol.items)
    # >>> [("a", 100), ("b", 200), ("c", 300)]

    sol.read("b")
    print(sol.items)
    # >>> [("b", 200), ("a", 100), ("c", 300)]

    sol.write("c", 350)
    print(sol.items)
    # >>> [("c", 350), ("a", 100), ("b", 200)]


if __name__ == "__main__":
    main()
