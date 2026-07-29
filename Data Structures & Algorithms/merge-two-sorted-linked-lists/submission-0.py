# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3 = ListNode(0)
        curr1 = list1
        curr2 = list2
        curr3 = list3

        while curr1 and curr2:
            if curr1 and curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            curr3 = curr3.next
        
        if curr1:
            curr3.next = curr1
        
        if curr2:
            curr3.next = curr2
        
        return list3.next



