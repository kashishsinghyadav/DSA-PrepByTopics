class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # node=r*n+c

        m=len(grid)
        n=len(grid[0])

        parent=[i for i in range(m*n)]
        rank=[0]*(m*n)

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            px=find(x)
            py=find(y)

            if px==py:
                return False

            if rank[px]>rank[py]:
                parent[py]=px
            elif rank[px]<rank[py]:
                parent[px]=py
            else:
                parent[px]=py
                rank[py]+=1

            return True

        # count total land cells
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    cnt+=1

        dirs=[(0,1),(1,0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':

                    for r,c in dirs:
                        nr=i+r
                        nc=j+c

                        if 0<=nr<m and 0<=nc<n and grid[nr][nc]=='1':

                            a=i*n+j
                            b=nr*n+nc

                            if union(a,b):
                                cnt-=1

        return cnt
        
