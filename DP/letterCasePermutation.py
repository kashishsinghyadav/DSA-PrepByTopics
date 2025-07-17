class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:

        def findsub(idx,ans,st):

            if len(st)==len(s):
                ans.append(st)
                return
            
            if idx>=len(s):
                return
            for i in range(idx,len(s)):
                curr=s[i]
                if curr.isalpha():
                    findsub(i+1,ans,st+curr.lower())
                    findsub(i+1,ans,st+curr.upper())
                else:
                    findsub(i+1,ans,st+s[i])                   

        ans=[]
        findsub(0,ans,'')
        return ans


        
