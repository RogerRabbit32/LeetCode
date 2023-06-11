class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        substring_pointer = 0
        for letter in t:
            if letter == s[substring_pointer]:
                substring_pointer += 1
                if substring_pointer == len(s):
                    return True
        return True if substring_pointer == len(s) else False
        