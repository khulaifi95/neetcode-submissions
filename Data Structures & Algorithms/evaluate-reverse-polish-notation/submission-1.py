class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch not in "+-*/":
                stack.append(ch)
            else:
                l = int(stack.pop())
                r = int(stack.pop())
                if ch == "+":
                    stack.append(l + r)
                elif ch == "-":
                    stack.append(r - l)
                elif ch == "*":
                    stack.append(r * l)
                elif ch == "/":
                    stack.append(r / l)
        return int(stack[-1])