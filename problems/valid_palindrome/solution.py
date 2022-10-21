class Solution:
    def isPalindrome(self, s: str) -> bool:
        final_string = ''
        for i in s:
            if not i.isalnum():
                pass
            else:
                final_string += i.lower()
        return True if final_string == final_string[::-1] else False