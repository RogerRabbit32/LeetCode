class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            new_n = self.countAndSay(n - 1)
            if len(new_n) == 1:
                return '1' + new_n
            result = ''
            current_symbol = new_n[0]
            count = 1
            for symbol in new_n[1:]:
                if symbol == current_symbol:
                    count += 1
                else:
                    result += str(count)
                    result += current_symbol
                    current_symbol = symbol
                    count = 1
            result += str(count)
            result += current_symbol
            return result