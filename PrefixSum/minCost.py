class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        maxi=0
        runsum=0
        for i in range(len(colors)-1):
            if colors[i]==colors[i+1]:
                maxi+=min(neededTime[i],neededTime[i+1])
                neededTime[i+1]=max(neededTime[i+1],neededTime[i])
        return maxi
        
