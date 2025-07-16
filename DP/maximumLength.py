class Solution:
    def maximumLength(self, nums: List[int]) -> int:

        n=len(nums)
        ans=0
        curr=0

        for i in range(n):
            if nums[i]%2==0:
                curr+=1

        # print(curr)
        ans=max(ans,curr)
        curr=0
        for i in range(n):
            if nums[i]%2!=0:
                curr+=1
        # print(curr)
        ans=max(ans,curr)
        curr=1
        prev=nums[0]%2
        for i in range(1,n):
            val=nums[i]%2
            if prev != val:
                curr+=1
                prev=val
        # print(curr)
        ans=max(ans,curr)
        return ans


        
