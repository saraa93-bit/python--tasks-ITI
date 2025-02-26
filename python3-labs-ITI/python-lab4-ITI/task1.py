# A Queue is a linear structure which follows a particular order in
#  which the operations are performed. The order is First In First Out
#  (FIFO). A good example of a queue is any queue of consumers for
#  a resource where the consumer that came first is served first.
#  1. We need to implement a python class that
#  represents the queue data structure. The class
#  should have these operations:
#  a. insert(value) => which inserts a new value at
#  the rear of the queue
#  b. pop() => which returns and removes a value
#  from the front of the queue. We should return
#  None and print a warning message if we tried
#  to pop value from an empty queue
#  c. is_empty() => which returns True or False to
#  represent whether the queue is empty or not.
 


class Queue:
    def __init__(self):
        self.items = []

    def insert(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            print(" Warning: The queue is empty.")
            return None
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


q = Queue()
q.insert(10)
q.insert(20)
print("Pop:", q.pop())
print("Is Empty?", q.is_empty())
q.pop()
q.pop()
