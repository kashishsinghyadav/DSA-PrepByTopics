class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        c=Counter(s)
        count=0
        if len(s)<k:
            return False
    
        for i,j in c.items():
            if j%2!=0:
                count+=1
        if count>k:
            return False
        return True

        
