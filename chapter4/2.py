class priorqueue():
    def __init__(self) :
        self.array=[0 for i in range(10)]
        self.size=0
    def isempty(self):
        if self.size==0:
            return True
    def isfull(self):
        if self.size==len(self.array):
            return True
    def enqueue(self,number):
        if self.isfull():
            raise Exception(' the queue is full')
        self.array[self.size]=number
        self.size+=1
    def dequeue(self):
        if self.isempty():
            raise Exception( 'the queue is empty ')
        max_v=max(self.array)
        index=self.array.index(max_v)
        for i in range(index,self.size):
            self.array[i]=self.array[i+1]
        self.size-=1
        return max_v
our=priorqueue()
our.enqueue(1)
our.enqueue(7)
our.enqueue(4)
our.enqueue(5)
print(our.dequeue())
print(our.dequeue())
print(our.dequeue())
print(our.dequeue())