class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        s_symbols = {}
        t_symbols = {}
        
        for symbol in s:
            if symbol in s_symbols:
                s_symbols[symbol] += 1
            else:
                s_symbols[symbol] = 1
        
        for symbol in t:
            if symbol in t_symbols:
                t_symbols[symbol] += 1
            else:
                t_symbols[symbol] = 1
        
        for symbol in t_symbols.keys():
            if symbol not in s_symbols or \
            s_symbols[symbol] != t_symbols[symbol]:
                return symbol
