"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        x = head
        while x:
            if x.child is None:
                x = x.next
            else:
                y = x.child
                z = x.next
                x.next = None
                x.next = y
                y.prev = x
                if z:
                    z.prev = None
                    while y.next:
                        y = y.next
                    y.next = z
                    z.prev = y
                x.child = None
                x = head
        return head
                