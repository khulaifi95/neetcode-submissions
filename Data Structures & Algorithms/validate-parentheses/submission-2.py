class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return
        stack = []
        for ch in s:
            if ch in "[({":
                stack.append(ch)
            elif ch == "]":
                if stack and stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif ch == "}":
                if stack and stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            elif ch == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    return False
        return True if not stack else False
                

