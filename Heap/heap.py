from collections import Counter
import heapq
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    maxHeap, dic, output = [] ,dict(Counter(nums)), []
    for key in dic: heapq.heappush(maxHeap, (-dic[key], key))
    for i in range(k): output.append(heapq.heappop(maxHeap)[1])
    return output

print(topKFrequent([1,1,1,2,2,3], 2))