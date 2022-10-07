class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        my_dict = {}
    
        for i in ransomNote:
            if i not in my_dict:
                my_dict[i] = 1
            else:
                my_dict[i] += 1

        for j in magazine:
            if j in my_dict:
                if my_dict[j] == 0:
                    pass
                else:
                    my_dict[j] -= 1
            else:
                pass

        if any(my_dict.values()):
            return False
        else:
            return True
