class twinQueue:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.array = [0] * capacity
        self.front1 = 0         
        self.back1 = 0          
        self.front2 = capacity 
        self.back2 = capacity  

    def enqueue1(self, value):
        if self.back1 < self.back2 - 1: 
            self.array[self.back1] = value
            self.back1 += 1
        else:
            raise Exception("Queue 1 is full")

    def enqueue2(self, value):
        if self.back1 < self.back2 - 1: 
            self.back2 -= 1
            self.array[self.back2] = value
        else:
            raise Exception("Queue 2 is full")

    def dequeue1(self):
        if self.front1 < self.back1:
            value = self.array[self.front1]
            self.front1 += 1
            return value
        else:
            raise Exception("Queue 1 is empty")

    def dequeue2(self):
        if self.front2 > self.back2:
            value = self.array[self.front2 - 1]
            self.front2 -= 1
            return value
        else:
            raise Exception("Queue 2 is empty")

    def is_empty1(self):
        return self.front1 == self.back1

    def is_empty2(self):
        return self.front2 == self.back2

    def is_full(self):
        return self.back1 == self.back2 - 1
