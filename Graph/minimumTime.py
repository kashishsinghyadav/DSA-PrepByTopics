
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        dire = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(grid)
        m = len(grid[0])

        if grid[0][1] > 1 and grid[1][0] > 1:
            return -1
        
        q = []
        heappush(q, (0, 0, 0))
        res = [[float('inf')] * m for _ in range(n)]
        res[0][0] = 0
        
        while q:
            currt, x, y = heappop(q)
            if x == n - 1 and y == m - 1:
                return currt
            for dx, dy in dire:
                newdx = dx + x
                newdy = dy + y
                if 0 <= newdx < n and 0 <= newdy < m:
                    wait = max(grid[newdx][newdy] - (currt + 1), 0)
                    if wait % 2 == 1:
                        wait += 1
                    new_cost = currt + 1 + wait
                    if new_cost < res[newdx][newdy]:
                        res[newdx][newdy] = new_cost
                        heappush(q, (new_cost, newdx, newdy))
        return -1
