class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack=[]
        n=len(pattern)+1
        ans=[]
        for i in range(n):
            stack.append(str(i+1))
           
            if i>=len(pattern) or pattern[i]=='I' :
                while stack:
                    ans.append(stack.pop())
        return ''.join(ans)
                
                
