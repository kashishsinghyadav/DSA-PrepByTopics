from collections import Counter
from heapq import heappush, heappop

class Solution:
    def findXSum(self, nums, k, x):
        c = Counter()
        ans = []
        l = 0
        
        for r in range(len(nums)):
            c[nums[r]] += 1
            
            if r - l + 1 == k:
                if len(c) < x:
                    ans.append(sum(nums[l:r+1]))
                else:
                    h = []
                    for i, j in c.items():
                        heappush(h, (-j, -i))
                    s = 0
                    f = x
                    while f:
                        cnt, val = heappop(h)
                        s += (-cnt) * (-val)
                        f -= 1
                    ans.append(s)
                
                c[nums[l]] -= 1
                if c[nums[l]] == 0:
                    del c[nums[l]]
                l += 1
        
        return ans
