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


def hot_potato(name_list, num):
    name_queue = Queue()

    for name in name_list:
        name_queue.enqueue(name)

    while name_queue.size() > 1:
        for i in range(num):
            name_queue.enqueue(name_queue.dequeue())
        name_queue.dequeue()

    return name_queue.dequeue()


print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Kent'], 7))
