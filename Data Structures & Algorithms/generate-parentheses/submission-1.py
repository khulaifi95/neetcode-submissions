class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(opend, closed):
            if opend == closed == n:
                res.append("".join(stack))
                return
            
            if opend < n:
                stack.append("(")
                backtrack(opend + 1, closed)
                stack.pop()
            if closed < opend:
                stack.append(")")
                backtrack(opend, closed + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res