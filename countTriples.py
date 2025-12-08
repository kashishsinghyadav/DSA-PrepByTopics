class Solution:
    def countTriples(self, n: int) -> int:
        ans=0
        for i in range(1,n):
            for j in range(i+1,n):
                s=i*i+j*j
                x=int(s**0.5)
                if x*x==s and x<=n:
                    ans+=1               

        return ans*2

        
