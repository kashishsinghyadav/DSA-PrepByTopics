class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        l = min(nums)
        r = max(nums)
        ans = r
        
        def findcap(nums, mid, k):
            cnt = 0
            i = 0
            while i < len(nums):
                if nums[i] <= mid:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k
        
        while l <= r:
            mid = l + (r - l) // 2
            if findcap(nums, mid, k):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans
