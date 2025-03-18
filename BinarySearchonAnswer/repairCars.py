class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def findmintime(mid,ranks):
            carfix=0
            for i in range(len(ranks)):
                carfix += int(math.sqrt(mid/ranks[i]))
            return carfix>=cars


        l=1
        r=max(ranks)*cars**2
        res=0
        while l<=r:
            mid = l+(r-l)//2
            if findmintime(mid,ranks):
                res=mid
                r=mid-1
            else:
                l=mid+1
        return res
        
