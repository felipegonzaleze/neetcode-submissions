class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        longest_prefix = ""
        i = 0
        for c in strs[0]:
            prefix += c
            i  += 1
            for str in strs:
                word = str[0:i]
                if prefix != word:
                    return longest_prefix
            longest_prefix = prefix[:]
        return longest_prefix