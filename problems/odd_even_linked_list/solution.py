# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        x = head
        newTail = ListNode()
        y = newTail
        while x and x.next:
            y.next = ListNode(x.next.val)
            y = y.next
            z = x.next.next
            x.next = None
            x.next = z
            x = x.next
        zh = head
        while zh.next:
            zh=zh.next
        zh.next = newTail.next
        return head