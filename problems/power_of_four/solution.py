class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        now_value = n
        while now_value > 1:
            now_value /= 4
        return True if now_value == 1 else False