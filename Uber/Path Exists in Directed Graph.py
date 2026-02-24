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
