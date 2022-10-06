class Solution:
    def repeatedCharacter(self, s: str) -> str:
        min = 0
        letter = ''
        for i in s:
            if s.count(i) > 1:
                now_min = s.index(i, s.index(i) + 1)
                if min == 0:
                    min = now_min
                    letter = i
                if now_min < min:
                    min = now_min
                    letter = i
        return letter
