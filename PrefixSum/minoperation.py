

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        lst = [i for i in range(len(boxes)) if boxes[i] == '1']
        ans = []
        for i in range(len(boxes)):
            ele = sum(abs(i - j) for j in lst)
            ans.append(ele)
        return ans
