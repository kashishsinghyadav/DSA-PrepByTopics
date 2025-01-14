class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        

        s1=set()
        s2=set()
        c=0
        res=[]
        for i in range(len(A)):
            if A[i] in s2:
                c+=1
            else:
                s1.add(A[i])
            if B[i] in s1:
                c+=1
            else:
                s2.add(B[i])
            res.append(c)
        return res
            
