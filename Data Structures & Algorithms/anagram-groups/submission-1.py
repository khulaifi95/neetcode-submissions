from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s2s = defaultdict(list)
        for s in strs:
            s2s["".join(sorted(s))].append(s)
        return [v for k, v in s2s.items()]