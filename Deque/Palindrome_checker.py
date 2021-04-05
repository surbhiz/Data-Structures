class Deque:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def get_queue(self):
        return self.items


def palindrome_check(a_string):
    char_deque = Deque()

    for char in a_string:
        char_deque.add_rear(char)

    chr_equal = True

    while char_deque.size() > 1 and chr_equal:
        first = char_deque.remove_front()
        second = char_deque.remove_rear()
        if first != second:
            chr_equal = False
    return chr_equal


print(palindrome_check('abba'))
print(palindrome_check('ladfksdnfn'))
print(palindrome_check('radar'))
