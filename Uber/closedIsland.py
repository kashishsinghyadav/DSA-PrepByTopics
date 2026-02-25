class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:





        n=len(grid)
        m=len(grid[0])
        vis=set()
        cnt=0

        def dfs(si,sj,vis):
            if si==0 or sj==0 or si==n-1 or sj==m-1:
                return False

            vis.add((si,sj))
            closed=True


            
            for r,c in [(0,1),(1,0),(-1,0),(0,-1)]:
                nr=r+si
                nc=c+sj
                if 0<=nr<n and 0<=nc<m and grid[nr][nc]==0 and (nr,nc) not in vis:
                    if not dfs(nr,nc,vis):
                        closed =False

            return closed



        for i in range(n):
            for j in range(m):
                if (i,j) not in vis and grid[i][j]==0:
                    if dfs(i,j,vis):
                        cnt+=1
        return cnt

        
