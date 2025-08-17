class Solution:
    def trapRainWater(self, h: List[List[int]]) -> int:
        m=len(h)
        n=len(h[0])
        heap=[]
        vis=set()

        for r in range(m):
            for c in [0,n-1]:
                heappush(heap,(h[r][c],(r,c)))
                vis.add((r,c))
        for c in range(n):
            for r in [0,m-1]:
                heappush(heap,(h[r][c],(r,c)))
                vis.add((r,c))
        water=0
        while heap:
            pp,idx=heappop(heap)

            for r,c in [(0,-1),(1,0),(-1,0),(0,1)]:
                i_=idx[0]+r
                j_=idx[1]+c
                if 0<i_<m and 0<j_<n and (i_,j_) not in vis:
                    water += max(pp-h[i_][j_],0)
                    heappush(heap,(max(pp,h[i_][j_]),(i_,j_)))
                    vis.add((i_,j_))
        return water



