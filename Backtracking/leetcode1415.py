class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def solve(n, curr, res):
            if len(curr) == n:
                res.append(curr)
                return
            for i in "abc":
                if not curr or curr[-1] != i:  
                    solve(n, curr + i, res)   

        res = []
        solve(n, "", res) 

        if k > len(res):   
            return ""

        return res[k - 1]  
