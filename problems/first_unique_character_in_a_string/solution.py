class Solution:
    def firstUniqChar(self, s: str) -> int:
        letter_count = {}
        
        for letter in s:
            if letter not in letter_count:
                letter_count[letter] = 1
            else:
                letter_count[letter] += 1
        
        for letter in letter_count:
            if letter_count[letter] == 1:
                return s.index(letter)
            
        return -1