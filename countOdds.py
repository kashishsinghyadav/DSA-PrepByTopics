class Solution:
    def countOdds(self, low: int, high: int) -> int:

        diff=high-low-1
        
        ans=0
        
           
        if diff%2==0:
            ans+= diff//2
            print(ans)

        else:
            
            if high%2==0 and low%2==0:
                ans+=diff//2+1
            else:
                ans+=diff//2
        if high%2==1:
            ans+=1
        if low%2==1:
            ans+=1
        return ans
