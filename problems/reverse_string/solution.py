class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        count = 0
        while count != len(s) - 1:
            s.insert(count, s[-1])
            s.pop()
            count += 1