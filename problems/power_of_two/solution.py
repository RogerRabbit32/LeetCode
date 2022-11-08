class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        now_value = n
        while now_value > 1:
            now_value /= 2
        return True if now_value == 1 else False