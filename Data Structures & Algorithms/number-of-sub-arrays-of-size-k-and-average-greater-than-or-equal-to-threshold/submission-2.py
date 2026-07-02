class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold *= k
        res = 0
        window = deque()

        L = 0
        for R in range(len(arr)):
            window.append(arr[R])
            if R - L + 1 < k:
                continue
            elif R - L + 1 > k:
                window.popleft()
                L += 1
            
            if R - L + 1 == k:
                if sum(window) >= threshold:
                    res += 1
        return res