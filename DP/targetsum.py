class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def find(i, s, dp, nums, n):
            if i == n:
                if s == target:
                    return 1
                else:
                    return 0
            if dp[i][s] != -1:
                return dp[i][s]

            left = find(i + 1, s + nums[i], dp, nums, n)
            right = find(i + 1, s - nums[i], dp, nums, n)
            dp[i][s] = left + right
            return dp[i][s]

        n = len(nums)
        maxi = sum(nums)
        dp = [[-1 for _ in range(maxi * 2 + 1)] for _ in range(n)]
        return find(0, 0, dp, nums, n)

        
