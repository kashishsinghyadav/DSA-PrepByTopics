class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        vis=set()

        def findPer(res,vis):
            nonlocal k
            
            if len(res)==n:
                k-=1
                if k<=0:
                    return res
                return 
            
                
            for i in range(1,n+1):
                
                if i not in vis:
                    vis.add(i)
                    res+=str(i)

                    x=findPer(res,vis)
                    if x:
                        return x
                    res=res[:-1]
                    vis.remove(i)
                    

        return findPer("",vis)
        

        
