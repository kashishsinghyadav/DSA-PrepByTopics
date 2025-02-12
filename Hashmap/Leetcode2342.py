class Solution:
    def getSum(self, num):
        s = 0
        for i in str(num):
            s += int(i)
        return s

    def maximumSum(self, nums: List[int]) -> int:
        d = defaultdict(list)
        for ch in nums:
            sumofDigit = self.getSum(ch)
            d[sumofDigit].append(ch)

        maximum = -1  

        for values in d.values():
            if len(values) >= 2:
                values.sort(reverse=True) 
                maximum = max(maximum, values[0] + values[1])  

        return maximum
