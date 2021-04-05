class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def get_stack(self):
        return self.items


s = Stack()
print(s.is_empty())
s.push(4)
s.push('Dog')

s.push('8.4')
print(s.peek())
print(s.is_empty())

s.pop()
s.pop()
print(s.peek())
print(s.size())


class StackusingList():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)


s1 = StackusingList()
print(s1.is_empty())
s1.push('Hello')
s1.push('System')
print(s1.peek())
s1.pop()
print(s1.peek())
