class Solution:
    def doesAliceWin(self, s: str) -> bool:
        v=0
        for i in s:
            if i in 'aeiou':
                v+=1
        if v==0:
            return False
        return True
        
