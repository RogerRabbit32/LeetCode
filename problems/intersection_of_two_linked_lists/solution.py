# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        node_count_A = 1
        x = headA
        while x.next:
            x = x.next
            node_count_A += 1
        node_count_B = 1
        y = headB
        while y.next:
            y = y.next
            node_count_B += 1
        
        if node_count_A > node_count_B:
            a = headA
            b = headB
            diff_node = node_count_A - node_count_B
            i = 0
            while i != diff_node:
                a = a.next
                i += 1
            while a != b and a.next and b.next:
                a = a.next
                b = b.next
            return a if a == b else None
        else:
            a = headA
            b = headB
            diff_node = node_count_B - node_count_A
            i = 0
            while i != diff_node:
                b = b.next
                i += 1
            while a != b and a.next and b.next:
                a = a.next
                b = b.next
            return a if a == b else None