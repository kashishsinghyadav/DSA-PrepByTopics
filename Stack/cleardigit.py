class Solution:
    def clearDigits(self, s: str) -> str:
        stack=[]
        
        for ch in s:
            if not ch.isdigit():
                stack.append(ch)
            if ch.isdigit():
                stack.pop()
        return ''.join(stack)

        
