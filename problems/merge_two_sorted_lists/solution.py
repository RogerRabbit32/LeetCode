# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0: int, next=None: Optional[ListNode]):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        result = []
        while list1 and list2:
            if list1.val>=list2.val:
                result.append(list2.val)
                list2 = list2.next
            else:
                result.append(list1.val)
                list1 = list1.next

        res = list1 if list1 else list2
        for i in result[::-1]:
            res = ListNode(val=i,next=res)

        return res
    


    