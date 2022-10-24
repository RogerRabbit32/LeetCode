class Solution:
    def isHappy(self, n: int) -> bool:
        
        old_result = n
        new_result = 0
        already_seen = []

        while True:
            for i in str(old_result):
                new_result += int(i) ** 2

            if new_result == 1:
                return True

            if new_result in already_seen:
                return False

            old_result = new_result
            already_seen.append(new_result)
            new_result = 0
