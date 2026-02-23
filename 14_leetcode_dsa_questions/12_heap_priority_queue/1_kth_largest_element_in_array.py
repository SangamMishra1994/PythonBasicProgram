import heapq
from typing import List


class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)

        return heap[0]


if __name__ == "__main__":
    nums, k = [3, 2, 1, 5, 6, 4], 2
    object = Solution1()
    print(f"Kth largest element :- {object.findKthLargest(nums, k)}")
