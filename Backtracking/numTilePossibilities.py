class Solution:
    def numTilePossibilities(self, tiles: str) -> int:

        def solve(curr,ans,used):
            ans.add(curr)

            for i in range(len(tiles)):
                if not used[i]:
                    used[i]=True
                    solve(curr+tiles[i],ans,used)
                    used[i]=False
                    
            
        used=[False]*len(tiles)
        ans=set()
        solve("",ans,used)
        return len(ans)-1
        
