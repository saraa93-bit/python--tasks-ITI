#  2. We need to implement another queue class that
#  has the same properties as previous but with the
#  following changes:
#  a. The queue should have a name that is
#  provided as a parameter of its constructor
#  b. The queue should have a size that is provided
#  as a parameter of its constructor and if we tried
#  to insert more values than its size raises a
#  custom exception called
#  QueueOutOfRangeException (BONUS)
#  Or raise IndexError with message .
# c. The queue keeps track with all queues
#  instances that has been created through this
#  class and we can get any queue of them using
#  its name.
#  d. D. The queue class should have two class
#  methods called (save, load) which saves all
#  created queues instances to a file and load
#  them when needed


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