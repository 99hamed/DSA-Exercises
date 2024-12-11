def remove_max(head):
        if not head:
            return 

        max_value = head.value
        current = head
        while current.next!=None:
            if current.value > max_value:
                max_value = current.value
            current = current.next

        
        current = head

       
        if head.value == max_value:
            head = head.next
            return

        
        while current.next.next!=None and current.next.value != max_value:
            current = current.next

        if current.next.next!=None:
            current.next = current.next.next
            
        