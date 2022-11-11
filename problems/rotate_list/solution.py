# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        size = 0
        x = head
        while x:
            size += 1
            x = x.next
        if k >= size:
            k = k % size
        while k != 0:
            x = head
            while x.next:
                x = x.next
            tail = x
            x = head
            while x.next != tail:
                x = x.next
            x.next = None
            tail.next = head
            head = tail
            k -= 1
        return head
        