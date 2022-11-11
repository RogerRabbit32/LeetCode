# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        size = 0
        pointer = head
        while pointer:
            size += 1
            pointer = pointer.next
        
        pointer = head
        curr = 1
        
        while curr != size // 2:
            pointer = pointer.next
            curr += 1
        
        return pointer.next
                       