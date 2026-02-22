
class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def bfs(src):
            dist = [-1] * n
            q = deque([src])
            dist[src] = 0

            while q:
                node = q.popleft()
                for neb in adj[node]:
                    if dist[neb] == -1:
                        dist[neb] = dist[node] + 1
                        q.append(neb)
            return dist
 
        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)
        # print(dx,dy,dz)
        cnt = 0
        for i in range(n):
            a, b, c = sorted([dx[i], dy[i], dz[i]])
            if a * a + b * b == c * c:
                cnt += 1

        return cnt
