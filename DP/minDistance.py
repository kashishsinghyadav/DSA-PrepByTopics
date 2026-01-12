class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m=len(word1)
        n=len(word2)
        memo=[[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if word1[i]==word2[j]:
                    memo[i+1][j+1]=memo[i][j]+1
                else:
                    memo[i+1][j+1]=max(memo[i][j+1],memo[i+1][j])
        lcs=memo[m][n]
        return m+n-2*lcs


        
