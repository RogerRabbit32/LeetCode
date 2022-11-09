# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or head.next is None:
            return False
        else:
            x = head
            y = head
            while x.next and y.next:
                x = x.next
                y = y.next
                if y.next:
                    y = y.next
                else:
                    return False
                if x == y:
                    return True