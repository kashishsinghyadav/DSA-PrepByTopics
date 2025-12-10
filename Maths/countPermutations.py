class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        
        for i in range(1,len(complexity)):
            if complexity[i]<=complexity[0]:
                return 0
        ans=math.factorial(len(complexity)-1) 
        mod=10**9+7
        return ans%mod
