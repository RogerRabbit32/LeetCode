# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        else:
            pointer = head
            size = 1
            while pointer.next:
                size += 1
                pointer = pointer.next
            pointer = head
            middle = 1
            while middle != size // 2:
                middle += 1
                pointer = pointer.next
            pointer.next = pointer.next.next
            return head