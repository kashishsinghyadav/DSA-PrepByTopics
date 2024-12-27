class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_values=0
        curr=0
        for i in range(1,len(values)):
            curr=max(curr,values[i-1]+i-1)
            max_values=max(max_values,curr+values[i]-i)
        return max_values
