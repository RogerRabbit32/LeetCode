# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        x = []
        while l1:
            x.append(l1.val)
            l1 = l1.next
        y = []
        while l2:
            y.append(l2.val)
            l2 = l2.next
        
        number1 = int(''.join([str(i) for i in x[::-1]]))
        number2 = int(''.join([str(i) for i in y[::-1]]))
        my_sum = number1 + number2
        dummy = list(str(my_sum)[::-1])
        
        result = ListNode()
        pointer = result
        for symbol in dummy:
            newNode = ListNode(symbol)
            pointer.next = newNode
            pointer = pointer.next
        
        return result.next
        
        
        