class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for i in range(len(words)):
            if words[i][0:len(pref)]==pref:
                count+=1
        return count
        
