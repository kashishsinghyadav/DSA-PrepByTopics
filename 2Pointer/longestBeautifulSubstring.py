class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        vowels = 'aeiou'
        l = 0
        ans = 0
        cnt = 1  # number of distinct vowels seen in order
        
        for r in range(1, len(word)):
            if word[r] < word[r - 1]:
                # Restart when order breaks
                l = r
                cnt = 1
            elif word[r] > word[r - 1]:
                # Only increase count when vowel changes to next in order
                cnt += 1
            
            # If all 5 vowels seen in order, update answer
            if cnt == 5:
                ans = max(ans, r - l + 1)
        
        return ans
