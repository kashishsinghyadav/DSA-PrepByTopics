class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        colormap=defaultdict(int)
        ballmap={}
        res=[]
        for x,y in queries:

            if x in ballmap:
                colormap[ballmap[x]] -= 1
                if colormap[ballmap[x]]==0:
                    del colormap[ballmap[x]]

            ballmap[x]=y
            colormap[y] += 1
            res.append(len(colormap))
        return res
