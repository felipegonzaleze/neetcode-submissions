class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            isEmpty = not bool(stack)
            if stack and c == ")" and stack[-1] == "(":
                stack.pop()
            elif stack and c == "}" and stack[-1] == "{":
                stack.pop()
            elif stack and c == "]" and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(c)
        if not stack:
            return True
        else:
            return False
            