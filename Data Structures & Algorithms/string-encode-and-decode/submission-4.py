class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:

        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            leng = int(s[i:j])
            word = s[j+1: j + 1 + leng]
            res.append(word)
            i = j + 1 + leng
        return res