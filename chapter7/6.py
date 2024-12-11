class Node:
    def __init__(self,a):
        self.value=a
        self.next=None
# alef
class link_stack1:
    def __init__(self,head):
        self.head=head
    def push(self,a):
        p=Node(a)
        p.next=self.head
        self.head=p
    def pop(self):
        value=self.head.value
        head=head.next
        return value
# part b
    class link_stack2:
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
#برای تابع اولی O(1)
#برای تابع دومی O(n)