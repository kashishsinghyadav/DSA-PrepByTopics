class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d=defaultdict(list)
        for u in range(len(accounts)):
            for v in range(1,len(accounts[u])):
                d[accounts[u][v]].append(u)
        # print(d)



        vis=set()
        res=[]

        def dfs(i,mail):
            if i in vis:
                return
            vis.add(i)

            for j in range(1,len(accounts[i])):
                mail.add(accounts[i][j])
                for neb in d[accounts[i][j]]:
                    dfs(neb,mail)

        for i, account in enumerate(accounts):
            if i not in vis:
                name,email=account[0],set()
                dfs(i,email)
                res.append([name]+sorted(email))
        return res



                

        
