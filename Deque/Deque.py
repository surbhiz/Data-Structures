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


d = Deque()
d.add_front('Surbhi')
d.add_front('Zambad')
d.add_rear('CSE')
d.add_rear('Hello')
print(d.is_empty())
d.remove_front()
d.remove_rear()
print(d.size())
print(d.get_queue())
