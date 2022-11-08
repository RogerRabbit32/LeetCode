class Solution:
    def addDigits(self, num: int) -> int:
        
        now_value = num
        
        while len(str(now_value)) != 1:
            result = 0
            for symbol in str(now_value):
                result += int(symbol)
            now_value = result
        
        return now_value