class Solution:
    def solve(self, board: List[List[str]]) -> None:

        if not board:
            return

        m,n=len(board),len(board[0])
        parent=[i for i in range(m*n+1)]

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            px=find(x)
            py=find(y)
            if px!=py:
                parent[px]=py

        dummy=m*n

        dirs=[(0,1),(1,0),(0,-1),(-1,0)]

        for i in range(m):
            for j in range(n):

                if board[i][j]=='O':

                    node=i*n+j

                    # boundary O
                    if i==0 or j==0 or i==m-1 or j==n-1:
                        union(node,dummy)

                    for dr,dc in dirs:
                        ni=i+dr
                        nj=j+dc

                        if 0<=ni<m and 0<=nj<n and board[ni][nj]=='O':
                            union(node,ni*n+nj)

        for i in range(m):
            for j in range(n):

                if board[i][j]=='O':

                    if find(i*n+j)!=find(dummy):
                        board[i][j]='X'
