# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return None
        else:
            x = head
            y = head
            while x.next and y.next:
                x = x.next
                y = y.next
                if y.next:
                    y = y.next
                else:
                    return None
                if x == y:
                    x = head
                    seen = set()
                    while True:
                        if x in seen:
                            return x
                        else:
                            seen.add(x)
                            x = x.next