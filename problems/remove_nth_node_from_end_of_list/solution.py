# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 1
        measurer = head
        while measurer.next:
            measurer = measurer.next
            size += 1
        if size == n:
            return head.next
        prev = size - n
        x = head
        count = 1
        while count != prev:
            x = x.next
            count += 1
        count = 1
        y = head
        while count != prev + 2:
            y = y.next
            count += 1
        x.next = y
        return head