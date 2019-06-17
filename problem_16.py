class Queue:
    def __init__(self):
        self.items = []

    def enQueue(self, item):
        self.items.insert(0, item)

    def deQueue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []


if __name__ == '__main__':
    q = Queue()
    q.enQueue(10)
    q.enQueue("himanshu")
    q.enQueue(4.4)
    q.deQueue()
    print(q.items)
