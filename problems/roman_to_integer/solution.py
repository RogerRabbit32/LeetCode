class Solution:
    def romanToInt(self, s: str) -> int:
        res = 0
        current_index = 0
        
        for _ in s:
            if _ == 'I':
                if current_index != int(len(s) - 1):
                    if s[current_index + 1] == 'V' or s[current_index + 1] == 'X':
                        pass
                    else:
                        res += 1
                else:
                    res += 1
            if _ == 'V':
                if current_index != 0:
                    if s[current_index - 1] == 'I':
                        res += 4
                    else:
                        res += 5
                else:
                    res += 5
            if _ == 'X':
                if current_index == len(s) - 1:
                    if s[current_index - 1] == 'I':
                        res += 9
                    else:
                        res += 10
                elif current_index != 0 and current_index != len(s) - 1:
                    if s[current_index - 1] == 'I':
                        res += 9
                    elif s[current_index + 1] == 'L' or s[current_index + 1] == 'C':
                        pass
                    else:
                        res += 10
                elif current_index == 0:
                    if s[current_index + 1] == 'L' or s[current_index + 1] == 'C':
                        pass
                    else:
                        res += 10
                else:
                    res += 10
            if _ == 'L':
                if current_index != 0:
                    if s[current_index - 1] == 'X':
                        res += 40
                    else:
                        res += 50
                else:
                    res += 50
            if _ == 'C':
                if current_index == len(s) - 1:
                    if s[current_index - 1] == 'X':
                        res += 90
                    else:
                        res += 100
                elif current_index != 0 and current_index != len(s) - 1:
                    if s[current_index - 1] == 'X':
                        res += 90
                    elif s[current_index + 1] == 'D' or s[current_index + 1] == 'M':
                        pass
                    else:
                        res += 100
                elif current_index == 0:
                    if s[current_index + 1] == 'D' or s[current_index + 1] == 'M':
                        pass
                    else:
                        res += 100
                else:
                    res += 100
            if _ == 'D':
                if current_index != 0:
                    if s[current_index - 1] == 'C':
                        res += 400
                    else:
                        res += 500
                else:
                    res += 500
            if _ == 'M':
                if current_index != 0:
                    if s[current_index - 1] == 'C':
                        res += 900
                    else:
                        res += 1000
                else:
                    res += 1000

            current_index += 1

        return res