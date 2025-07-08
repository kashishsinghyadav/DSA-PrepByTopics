class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        n = len(events)
        dp = {}

        def findevent(end):
            low, high = 0, n
            while low < high:
                mid = (low + high) // 2
                if events[mid][0] > end:
                    high = mid
                else:
                    low = mid + 1
            return low

        def maxisum(i, k):
            if i >= n or k == 0:
                return 0
            if (i, k) in dp:
                return dp[(i, k)]

            start, end, val = events[i]
            nottake = maxisum(i + 1, k)
            next_event_index = findevent(end)
            take = val + maxisum(next_event_index, k - 1)

            dp[(i, k)] = max(take, nottake)
            return dp[(i, k)]

        return maxisum(0, k)
