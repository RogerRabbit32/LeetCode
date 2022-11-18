class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern_dict = {}
        pattern_structure = []
        i = 0
        for symbol in pattern:
            if symbol not in pattern_dict.keys():
                pattern_dict[symbol] = i
                pattern_structure.append(i)
                i += 1
            else:
                pattern_structure.append(pattern_dict[symbol])
        
        s_dict = {}
        s_structure = []
        i = 0
        for symbol in s.split():
            if symbol not in s_dict.keys():
                s_dict[symbol] = i
                s_structure.append(i)
                i += 1
            else:
                s_structure.append(s_dict[symbol])
        
        return pattern_structure == s_structure