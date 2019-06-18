'''
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, 
with the following API:

record(order_id): adds the order_id to the log
get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.
'''


class Queue:
    def __init__(self, s):
        self.items = []
        self.s = s

    def enQueue(self, item):
        #print("size of queue : " + str(self.s))
        #print("current item : " + str(self.size()))
        if self.size() >= self.s:
            self.deQueue()
        self.items.insert(0, item)

    def deQueue(self):
        if not self.isEmpty():
            self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    # time/space complexity : O(1)/O(N)
    def record(self, item):
        if self.size() >= self.s:
            self.deQueue()
        self.enQueue(item)

    # time/space complexity : O(N)/nil
    def get_last(self, nbr):
        print(self.items[-nbr:])


if __name__ == '__main__':
    q = Queue(5)
    q.enQueue(10)
    q.enQueue("Tinku")
    q.enQueue(4.4)
    print(q.items)
    q.record(20)
    q.record("Rinku")
    q.record("5.5")
    print(q.items)
    q.get_last(1)
    q.get_last(2)
    q.get_last(3)
