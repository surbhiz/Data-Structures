class Queue:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def get_queue(self):
        return self.items


q = Queue()
q.enqueue('Surbhi')
q.enqueue('Zambad')
q.enqueue('CSE')
print(q.is_empty())
q.dequeue()
print(q.size())
print(q.get_queue())
