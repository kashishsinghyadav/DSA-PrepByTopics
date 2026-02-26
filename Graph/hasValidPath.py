

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        streets = {
            1: [(0, -1), (0, 1)],     # left, right
            2: [(-1, 0), (1, 0)],     # up, down
            3: [(0, -1), (1, 0)],     # left, down
            4: [(0, 1), (1, 0)],      # right, down
            5: [(0, -1), (-1, 0)],    # left, up
            6: [(0, 1), (-1, 0)]      # right, up
        }

        m, n = len(grid), len(grid[0])

        q = deque()
        q.append((0, 0))
        vis = {(0, 0)}

        while q:
            r, c = q.popleft()

            if r == m - 1 and c == n - 1:
                return True

            for dr, dc in streets[grid[r][c]]:
                newr = r + dr
                newc = c + dc

                if 0 <= newr < m and 0 <= newc < n and (newr, newc) not in vis:
                    if (-dr, -dc) in streets[grid[newr][newc]]:
                        vis.add((newr, newc))
                        q.append((newr, newc))

        return False
