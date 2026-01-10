class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = [[0 for _ in range(len(s1) + 1)] for _ in range(len(s2) + 1)]
        r=len(s2)
        c=len(s1)
        for j in range(len(s2)):
            for i in range(len(s1)):
                if s1[i] == s2[j]:
                    memo[j+1][i+1] = memo[j][i] + ord(s1[i])
                else:
                    memo[j+1][i+1] = max(memo[j+1][i], memo[j][i+1])
        maxi=memo[r][c]
        # print(maxi)
        s=0
        for i in s1:
            s+=ord(i)
        for j in s2:
            s+=ord(j)
        return s-(2*maxi)
