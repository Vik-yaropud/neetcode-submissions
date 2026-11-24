import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
    return heap[0]

def get_min_4_elements(arr: List[int]) -> List[int]:
    heap = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
    return heapq.nsmallest(4, heap)


def get_min_2_elements(arr: List[int]) -> List[int]:
    heap = []
    new_heap = []
    results = []
    for i in range(len(arr)):
        heapq.heappush(heap, arr[i])
    for i in range(2):
        value = heapq.heappop(heap)
        heapq.heappush(new_heap, -value)
    while new_heap:
        results.append(-(heapq.heappop(new_heap)))
    return results

# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

