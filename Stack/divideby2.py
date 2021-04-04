class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def get_stack(self):
        return self.items


def divideby2(dec_no):
    rem_stack = Stack()

    while dec_no > 0:
        rem = dec_no % 2
        rem_stack.push(rem)
        dec_no = dec_no//2

    bin_str = ""
    while not rem_stack.is_empty():
        bin_str = bin_str+str(rem_stack.pop())

    return bin_str


def baseconverter(deci_no, base):
    digits = "0123456789ABCDEF"
    remi_stack = Stack()

    while deci_no > 0:
        remi = deci_no % base
        remi_stack.push(remi)
        deci_no = deci_no//base

    new_str = ""
    while not remi_stack.is_empty():
        new_str = new_str+digits[remi_stack.pop()]

    return new_str


print(divideby2(25))
print(baseconverter(256, 16))
