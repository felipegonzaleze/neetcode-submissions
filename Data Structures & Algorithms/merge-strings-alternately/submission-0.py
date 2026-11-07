class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final_string = ""
        w1_pointer = 0
        w2_pointer = 0
        while w1_pointer <= len(word1) - 1 and w2_pointer <= len(word2) - 1:
            final_string += word1[w1_pointer] + word2[w2_pointer]
            w1_pointer += 1
            w2_pointer += 1
        final_string += word1[w1_pointer:] + word2[w2_pointer:]
        return final_string  