class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([ch for ch in s if ch.isalnum()])
        return s.lower() == s[::-1].lower()