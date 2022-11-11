# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None
        x = head
        while x.next:   
            if x.next.val != val:
                x = x.next
            else:
                y = x.next
                x.next = None
                y = y.next
                x.next = y
        if x.val == val:
            return None
        if head.val == val:
            head = head.next
        return head
        