class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        count = 0
        for i in range(len(strs[0])):
            for word in strs:
                if word[i] == strs[0][i]:
                    pass
                else:
                    return strs[0][:count]
            count += 1
        return strs[0][:count]
