class Node:
    def __init__(self,a):
        self.value=a
        self.next=None
class link_stack:
    def __init__(self,head):
        self.head=head
    def push(self,a):
        p=self.head
        q=Node(a)
        while p.next!=None:
            p=p.next
        p.next=q
        q.next=None
    def pop(self):
        p=self.head
        while p.next.next!=None:
            p=p.next
        value=p.next.value
        p.naxt=None
        return value
        

        
        