class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        Q = len(queries)

        def checkallzero(diff, nums, queries, k):
            diff[:] = [0] * len(nums)
            for i in range(k + 1):
                l = queries[i][0]
                r = queries[i][1]
                wt = queries[i][2]
                diff[l] += wt
                if r + 1 < n:
                    diff[r + 1] -= wt

            cs = 0
            for i in range(n):
                cs += diff[i]
                if nums[i] - cs > 0:
                    return False
            return True

        if all(x == 0 for x in nums):
            return 0

        diff = [0] * n
        left=0
        right=Q-1
        ans=-1
        while left<=right:
            mid= left+(right-left)//2
            if checkallzero(diff, nums, queries, mid):
                ans=mid+1
                right=mid-1
            else:
                left = mid + 1
        return ans
