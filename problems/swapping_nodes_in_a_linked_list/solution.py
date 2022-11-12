# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        k1 = 0
        k2 = 0
        size = 1 
        
        pointer = head
        while pointer.next:
            size += 1
            pointer = pointer.next
        
        if size == k:
            count = 1
            pointer = head
            while count != k:
                pointer = pointer.next
                count += 1
            
            val1 = pointer.val
            pointer = head
            val2 = pointer.val
            pointer.val = val1
            count = 1
            while count != k:
                pointer = pointer.next
                count += 1
            pointer.val = val2
            return head
        
        head_index = 1
        pointer = head
        while head_index != k:
            pointer = pointer.next
            head_index += 1
        k1 = pointer.val
        
        tail_index = 1
        pointer = head
        while tail_index != size - k:
            pointer = pointer.next
            tail_index += 1
        k2 = pointer.next.val
        
        pointer = head
        head_index = 1
        while head_index != k:
            pointer = pointer.next
            head_index += 1
        pointer.val = k2
        
        pointer = head
        tail_index = 1
        while tail_index != size - k:
            pointer = pointer.next
            tail_index += 1
        pointer.next.val = k1
        
        return head
        
        
        
        