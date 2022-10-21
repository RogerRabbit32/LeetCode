class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        check = 1
        
        while check < n:
            check *= 3
        
        return True if n == check else False