
class Solution:
    def minTimeToReach(self, move):
        dire = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n = len(move)
        m = len(move[0])

        q = []
        heappush(q, (0, 0, 0))
        res = [[float('inf')] * m for _ in range(n)]
        res[0][0] = 0

        while q:
            curr_time, x, y = heappop(q)
            if x == n - 1 and y == m - 1:
                return curr_time
            for dx, dy in dire:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    wait = max(move[nx][ny] - curr_time, 0)
                    new_cost = curr_time + wait + 1
                    if new_cost < res[nx][ny]:
                        res[nx][ny] = new_cost
                        heappush(q, (new_cost, nx, ny))
        return -1
