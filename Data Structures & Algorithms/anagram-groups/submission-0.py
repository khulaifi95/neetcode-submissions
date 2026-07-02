from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        all_cnt = defaultdict(list)
        for one in strs:
            one_cnt = [0 for _ in range(26)]
            for ch in one:
                one_cnt[ord(ch) - ord('a')] += 1
            all_cnt[tuple(one_cnt)].append(one)
        return list(all_cnt.values())