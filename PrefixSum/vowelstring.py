class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        ans = [0] * (len(words) + 1)
        for i in range(len(words)):
            ans[i + 1] = ans[i] + (1 if words[i][0] in vowels and words[i][-1] in vowels else 0)
        res = []
        for start, end in queries:
            res.append(ans[end + 1] - ans[start])
        return res

        
