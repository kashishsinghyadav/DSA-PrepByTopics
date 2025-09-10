

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        d = defaultdict(set)
        for i, langs in enumerate(languages):
            d[i+1] = set(langs)

        teach=set()
        for u,v in friendships:
            if len(d[u]&d[v])==0:
                teach.add(u)
                teach.add(v)
        ans=float('inf')


        for i in range(1,n+1):
            cnt=0
            for user in teach:
                if i not in d[user]:
                    cnt+=1
            ans=min(ans,cnt)
        return ans
            
        
        
