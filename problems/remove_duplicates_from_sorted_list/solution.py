# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        pointer = head
        while pointer.next:
            if pointer.val == pointer.next.val:
                newtail = pointer.next.next
                pointer.next = newtail
            else:
                pointer = pointer.next
        return head