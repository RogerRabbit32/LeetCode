class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        letters_count = {}
        
        for letter in s:
            if letter in letters_count:
                letters_count[letter] += 1
            else:
                letters_count[letter] = 1
        
        result = 0
        
        for letter in letters_count.keys():
            if letters_count[letter] % 2 == 1:
                result += letters_count[letter] - 1
            else:
                result += letters_count[letter]
            
        for value in letters_count.values():
            if value % 2 != 0:
                result += 1
                return result
        
        return result