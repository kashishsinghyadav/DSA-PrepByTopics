class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxi=-1e9
        n=len(s)
        dp= [[-1] * n for _ in range(n)]
        def solve(s,i,j):
            if i>=j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j] = solve(s,i+1,j-1)
                return dp[i][j]
            
            dp[i][j]=0
            return dp[i][j]
        st=''
        idx=0
        for i in range(len(s)):
            for j in range(i,len(s)):
                if solve(s,i,j):
                    if j-i+1> maxi:

                        maxi=j-i+1
                        idx=i
                        
        return s[idx:maxi+idx]
         

       
        
