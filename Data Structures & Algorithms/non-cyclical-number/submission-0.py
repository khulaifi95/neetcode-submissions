"""
n -> sum(digits ** 2)

100 -> 1

101 -> 2

"""

class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.helper(n)
            if n == 1:
                return True
        return False
    
    def helper(self, n: int) -> int:
        res = 0

        while n:
            dig = n % 10
            dig = dig ** 2
            res += dig
            n = n // 10
        return res