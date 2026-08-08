# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #traverse the list, store the vals, reverse and add. reverse again and form lists

        tempHead = ListNode(0)
        curr = tempHead
        carry = 0

        while l1 or l2 or carry != 0:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            added = x + y + carry
            carry = added//10

            new_node = ListNode(added%10)
            curr.next = new_node
            curr = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return tempHead.next
        