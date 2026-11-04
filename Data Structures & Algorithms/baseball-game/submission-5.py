class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations:
            if op.lstrip('-').replace('.', '', 1).isdigit():
                stack.append(int(op))
            elif op == "+":
                if len(stack) >= 2:
                    stack.append(stack[-1] + stack[-2])
            elif op == "C":
                if stack:
                    stack.pop()
            elif op == "D":
                if stack:
                    stack.append(2 * stack[-1])
            print(stack)
        return sum(stack)