class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Step 1: Sort intervals by start time
        # Ensures we process intervals in order for greedy/backtracking
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        
        # Step 2: Iterate through remaining intervals starting from index 1
        for start, end in intervals[1:]:
            # Step 3a: Check if current interval does NOT overlap with previous
            # Non-overlapping condition: start >= prevEnd
            if start >= prevEnd:
                # BACKTRACK CHOICE 1: KEEP this interval
                # - No removal needed
                # - Update prevEnd to this interval's end
                # - Move forward (loop continues to next interval)
                prevEnd = end
            else:
                # Step 3b: Current interval OVERLAPS with previous
                # BACKTRACK CHOICE 2: We must remove one of them
                # - Increment removal count
                res += 1
                
                # Step 3c: Decide which interval to remove
                # Keep the one with earlier ending time (greedy decision)
                # This leaves more room for future intervals
                # Update prevEnd to the minimum of both endings
                prevEnd = min(end, prevEnd)
        
        # Step 4: Return total number of intervals removed
        return res