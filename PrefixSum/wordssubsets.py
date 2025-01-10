class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        ans = set(words1)
        chars = {}
        for sub in words2:
            for char in sub:
                count = sub.count(char)
                if char not in chars or count > chars[char]:
                    chars[char] = count
        for word in words1:
            for char in chars:
                if word.count(char) < chars[char]:
                    ans.remove(word)
                    break
        return list(ans)
