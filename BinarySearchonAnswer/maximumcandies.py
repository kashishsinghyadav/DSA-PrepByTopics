class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        
        l=1
        maxi=max(candies)
        ans=0
        r=maxi
        if sum(candies)<k:
            return 0 
      
        def check(candies,mid):
            cnt=0
            for i in range(len(candies)):
                cnt += candies[i]//mid
            return cnt>=k
        while l<=r:
            mid = l+(r-l) // 2
            if mid==0:
                break
            if check(candies,mid):
                ans=mid
                l=mid+1
            else:
                r=mid-1
        return ans
