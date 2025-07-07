

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        n = len(events)
        i = 0
        heap = []
        day = 0
        cnt = 0

        while i < n or heap:
            if not heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heappush(heap, events[i][1])
                i += 1

            if heap:
                heappop(heap)
                cnt += 1
                day += 1

            while heap and heap[0] < day:
                heappop(heap)

        return cnt


        
