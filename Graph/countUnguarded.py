class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        cell=[[0 for _ in range(n)] for _ in range(m)]
        for i,j in guards:
            cell[i][j]=-1
        for i,j in walls:
            cell[i][j]=-1

        for x,y in guards:

            for i,j in [(0,1),(-1,0),(1,0),(0,-1)]:
                nr=i+x
                nc=j+y
                while 0<=nr<m and 0<=nc<n and cell[nr][nc]!=-1:
                    cell[nr][nc]=2
                    nr+=i
                    nc+=j
        return sum(cell[i][j]==0 for i in range(m) for j in range(n) )
                


        
        



        
