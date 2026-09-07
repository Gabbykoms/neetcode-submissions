# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        #printing out thel list to verify
        read = head
        while read:
            print(read.val)
            read = read.next

        #finding the second half of the list
        slow_ptr = head
        fast_ptr = head

        while fast_ptr and fast_ptr.next:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        print("this is slow", slow_ptr.val)

        print("mid", slow_ptr.val)

        #reversing the second part of the list
        second = slow_ptr.next
        slow_ptr.next = None

        prev = None
        curr = second
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        half_head = prev

        first, second = head, prev
        

        while first and second:
            temp1 = first.next 
            temp2 = second.next 

            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2
        


        

        
        
        