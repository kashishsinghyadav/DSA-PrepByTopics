class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        d={}
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]-i in d:
                d[nums[i]-i] += 1
            else:
                d[nums[i]-i] = 1
        result=0
        for key,val in d.items():
            if val>1:
                result += (val*(val-1))//2
        return (n*(n-1))//2 - result
        
