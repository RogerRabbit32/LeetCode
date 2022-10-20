class Solution:
    def mySqrt(self, x: int) -> int:
        y = 0
        while y * y < x:
            y += 1
        return y if y * y == x else y - 1
        