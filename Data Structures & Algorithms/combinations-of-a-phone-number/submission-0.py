class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig2char = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }

        res = []
        curr = []

        def backtrack(i):
            if i >= len(digits):
                if curr:
                    res.append("".join(curr.copy()))
                return
            
            for ch in dig2char[int(digits[i])]:
                curr.append(ch)
                backtrack(i + 1)
                curr.pop()

        backtrack(0)

        return res        