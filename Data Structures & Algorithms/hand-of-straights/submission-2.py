class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        cnt = Counter(hand)

        for num in hand:
            start = num
            while cnt[start - 1]:
                start -= 1
            while start <= num:
                while cnt[start]:
                    for i in range(start, start + groupSize):
                        if not cnt[i]:
                            return False
                        cnt[i] -= 1
                start += 1
        return True