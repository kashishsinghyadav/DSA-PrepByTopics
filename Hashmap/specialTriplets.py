class Solution:
    def specialTriplets(self, a: List[int]) -> int:
        m=10**9+7
        r={}
        for x in a:
            r[x]=r.get(x,0)+1
        l={}
        s=0
        for x in a:
            r[x]-=1
            t=x*2
            s=(s+l.get(t,0)*r.get(t,0))%m
            l[x]=l.get(x,0)+1
        return s
