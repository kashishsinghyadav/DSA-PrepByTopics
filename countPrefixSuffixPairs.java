class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        ans = 0

        def isPrefixAndSuffix(a, b):
            if len(a) > len(b):
                return False
            return b[:len(a)] == a and b[-len(a):] == a

        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    ans += 1

        return ans
