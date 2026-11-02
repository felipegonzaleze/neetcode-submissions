class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        word = ""
        reversed = ""
        for c in s:
            if c.isalnum():
                word += c
        for c in word:
            reversed = c + reversed
        if word == reversed:
            return True
        return False