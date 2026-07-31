# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        llen = 0
        cur = head
        while cur:
            print("-->", cur.val)
            llen += 1
            cur = cur.next
        print("the length", llen)


        llen_use = llen - n
        if llen_use == 0:
            return head.next
        
        rem = head
        for _ in range(llen_use-1):
            rem = rem.next
        rem.next = rem.next.next
                
          
        
        
        return head
        