
def circular(head):
    p=head
    while p.next!=None:
        p=p.next
    p.next=head
    head.pre=p
