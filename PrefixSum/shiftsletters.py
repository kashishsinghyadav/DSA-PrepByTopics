class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        summ = [0 for _ in range(len(s)+1)]
        
        for st, end, d in shifts:
            if d == 0:
                summ[st] -= 1
                summ[end+1] += 1
            else:
                summ[st] += 1
                summ[end+1] -= 1
        
        csum= 0
        for i in range(len(s)):
            csum += summ[i]
            
            new = (((ord(s[i]) + csum) - 97) % 26) + 97
            s = s[:i] + chr(new) + s[i+1:]
        
        return s
