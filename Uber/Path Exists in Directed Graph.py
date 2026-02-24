class Solution:
    def pathExists(self, adjList: List[List[int]]) -> bool:
        n = len(adjList)

        def dfs(src, vis):
            vis.add(src)
            for neb in adjList[src]:
                if neb not in vis:
                    dfs(neb, vis)

        vis = set()
        dfs(0, vis)
        return (n - 1) in vis



class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        rank = [0]*n
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(p1, p2):
            px = find(p1)
            py = find(p2)

            if px == py:
                return

            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1

        for u, v in edges:
            union(u, v)

        return find(source) == find(destination)
