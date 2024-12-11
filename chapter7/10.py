#seems like bubble sort
def sort(head):
    p=head
    
    while p.next!=None:
        while p.next.next!=None:
            if p.next.value<p.value:
                k=head
                while k.next!=p:
                    k=k.next
                k.next=p.next
                p.next=p.next.next
                

