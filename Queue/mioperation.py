

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        cnt = 0
        
        for num in nums:
            heappush(heap, num)  
        
        while len(heap) >1  and heap[0] < k:
            x = heappop(heap)
            y = heappop(heap)
            
            heappush(heap, 2*min(x,y)+max(x,y))
            
           
            cnt += 1
        
        return cnt
