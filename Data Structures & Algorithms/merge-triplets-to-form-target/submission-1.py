"""
triplets[i] = [ai, bi, ci]
-> target = [x, y, z]

operations: element max

[
[1, 2, 3],
[7, 1, 1]
]

[7, 2, 3]
"""


class Solution:

    def is_valid_for_max_out(self, a, b):
        for i in range(len(a)):
            if a[i] > b[i]:
                return False
        return True

    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        valid = [trip for trip in triplets if self.is_valid_for_max_out(trip, target)]
        for one in valid:
            for i, v in enumerate(one):
                if v == target[i]:
                    good.add(i)
        return len(good) == 3
