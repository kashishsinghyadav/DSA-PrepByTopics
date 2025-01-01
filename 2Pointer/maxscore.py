class Solution:
    def maxScore(self, s: str) -> int:
        maxi=0
        for i in range(len(s)-1):
            left=s[:i+1].count('0')
            right=s[i+1:].count('1')
            maxi=max(maxi,left+right)
        return maxi
        
        
