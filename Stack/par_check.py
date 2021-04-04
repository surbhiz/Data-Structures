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


def par_check(symbol_str):
    s = Stack()
    balance = True
    index = 0
    while index < len(symbol_str) and balance:
        symbol = symbol_str[index]

        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

        index = index+1

    if balance and s.is_empty():
        return True
    else:
        return False


print(par_check("(())))"))
print(par_check("(())"))
