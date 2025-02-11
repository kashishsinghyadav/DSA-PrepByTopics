class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        
        stack=[]
        n=len(part)
        for ch in s:
            stack.append(ch)
            while len(stack)>=len(part) and ''.join(stack[-n:])==part:
                del stack[-n:]
        return ''.join(stack)
