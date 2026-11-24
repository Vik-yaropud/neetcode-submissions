import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    heap = []
    results = []

    for i in nums:
        pair = (-i, i)
        heapq.heappush(heap, pair)

    while heap:
        pair = heapq.heappop(heap)
        value = pair[1]
        results.append(value)
    return results

# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
