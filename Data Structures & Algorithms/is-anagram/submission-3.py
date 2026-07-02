
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = [0 for _ in range(26)]
        c2 = [0 for _ in range(26)]
        for ch in s:
            idx = ord(ch) - ord('a')
            c1[idx] += 1
        for ch in t:
            idx = ord(ch) - ord('a')
            c2[idx] += 1
        return c1 == c2