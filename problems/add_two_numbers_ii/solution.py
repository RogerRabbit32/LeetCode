# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1
        number1 = []
        while x:
            number1.append(str(x.val))
            x = x.next
        y = l2
        number2 = []
        while y:
            number2.append(str(y.val))
            y = y.next
        
        number1 = int(''.join(number1))
        number2 = int(''.join(number2))
        my_sum = list(str(number1 + number2))
        
        result = ListNode()
        z = result
        
        for symbol in my_sum:
            x = ListNode(symbol)
            z.next = x
            z = z.next
        
        return result.next
        
        
        