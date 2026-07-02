class Solution:

    def isParlindrome(self, ss: str, l, r):
        
        while l < r:
            if ss[l] != ss[r]:
                return False
            l += 1
            r -= 1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res, carry = [], []

        def dfs(j, i):
            # this is one step dfs here over
            # at each step, we split the current string
            # options: given length n, we have n - 1 ways to cut in 2
            # choice: for each half of the string, do it again
            # limits: u cannot have an empty string
            # base case: for a valid string, check isParlindrome (single char works)
            # if at base case, we shall: append the current splits to res
            # if not, we shall: update the carried results

            if i >= len(s):
                if i == j:
                    res.append(carry.copy())
                return


            if self.isParlindrome(s, j, i):
                carry.append(s[j: i + 1])
                dfs(i + 1, i + 1)
                carry.pop()
            
            dfs(j, i + 1)
        
        dfs(0, 0)
        return res
            
