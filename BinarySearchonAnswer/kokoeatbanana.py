class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxi=max(piles)
        n=len(piles)


        def cal(piles,t):
            total=0
            for i in range(n):
                total += math.ceil(piles[i]/t)
            return total


        l=1
        while l<=maxi:
            mid=(l+maxi)//2
            totalhours=cal(piles,mid)
            if totalhours<=h:
                maxi=mid-1
            else:
                l=mid+1
        return l
