class Node:
    def __init__(self,a):
        self.value=a
        self.next=None
        self.pre=None
class prioity_queue:
    def __init__(self,head):
        self.head=head
    def enqueue(self,a):
        curr=self.head
        p=Node(a)
        while curr.next!=None:
            curr=curr.next
        curr.next=p
        p.next=None
        p.pre=curr
    def dequeue(self):
        min=self.head
        p=self.head.next
        while p !=None:
            if min.value>p.value:
                min=p
            p=p.next
        if min.pre==None:
            head=min.next
            head.pre=None
        elif min.next==None:
            min.pre.next=None
        else:
            min.pre.next=min.next
            min.next.pre=min.pre
        return min.value
    # b part
    def sort(self,n):
        for i in range(n):
            self.enqueue(int(input()))
        for j in range(n):
            print(self.dequeue())

