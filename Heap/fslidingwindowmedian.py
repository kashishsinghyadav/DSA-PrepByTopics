

def medianSlidingWindow(nums: List[int], k: int) -> List[float]:
    if not nums or not k:
        return []

    lo = []   
    hi = []  
    to_remove = defaultdict(int)

    for i in range(k):
        if len(lo) == len(hi):
            heapq.heappush(hi, -heapq.heappushpop(lo, -nums[i]))
        else:
            heapq.heappush(lo, -heapq.heappushpop(hi, nums[i]))

    ans = [float(hi[0])] if k % 2 == 1 else [(hi[0] - lo[0]) / 2.0]

    for i in range(k, len(nums)):
        in_num = nums[i]
        out_num = nums[i - k]

        heapq.heappush(lo, -heapq.heappushpop(hi, in_num))

        if out_num > -lo[0]:
            heapq.heappush(hi, -heapq.heappop(lo))

        to_remove[out_num] += 1

        while lo and to_remove[-lo[0]]:
            to_remove[-lo[0]] -= 1
            heapq.heappop(lo)

        while hi and to_remove[hi[0]]:
            to_remove[hi[0]] -= 1
            heapq.heappop(hi)

        if k % 2 == 1:
            ans.append(float(hi[0]))
        else:
            ans.append((hi[0] - lo[0]) / 2.0)

    return ans
