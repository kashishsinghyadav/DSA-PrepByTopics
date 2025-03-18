class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff=[0]*len(nums)
        if all(x == 0 for x in nums):
            return 0
        for i in range(len(queries)):
            l=queries[i][0]
            r=queries[i][1]
            diff[l] += 1
            if (r+1)<len(diff):
                diff[r+1] -= 1
        curr=0
        for i in range(len(diff)):
            curr += diff[i]
            
            if nums[i]-curr > 0:
                return False
        return True

        
