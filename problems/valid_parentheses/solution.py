class Solution:
    def isValid(self, s: str) -> bool:
        
        correct_order_brackets = {'(': ')', '[': ']', '{': '}'}
        opening_brackets = []
        
        for bracket in s:
            if bracket in correct_order_brackets.keys():
                opening_brackets.append(bracket)
            else:
                if not opening_brackets or \
                bracket != correct_order_brackets[opening_brackets[-1]]:
                    return False
                else:
                    opening_brackets.pop()
                    
        return True if not opening_brackets else False
            
