class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n = len(nums) - k + 1
        pref = [0] * n
        pref[0] = sum(nums[:k])
        for i in range(1, n):
            pref[i] = pref[i-1] - nums[i-1] + nums[i+k-1]
        h = [(-pref[i], i) for i in range(k+k, n)]
        heapify(h)
        first, second, third = 0, k, k+k
        curr_max = pref[first] + pref[second] + pref[third]
        left = 0
        for mid in range(k, n - k):
            if pref[mid - k] > pref[left]:
                left = mid - k
            while h[0][1] < mid + k:
                heappop(h)
            t = pref[left] + pref[mid] - h[0][0]
            if t > curr_max:
                curr_max = t
                first, second, third = left, mid, h[0][1]
        return [first, second, third]
