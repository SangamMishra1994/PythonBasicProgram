import heapq
from typing import List


class Solution3:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = sorted(zip(nums1, nums2), key=lambda x: -x[1])

        heap = []
        total_sum = 0
        max_score = 0

        for n1, n2 in pairs:
            heapq.heappush(heap, n1)
            total_sum += n1

            if len(heap) > k:
                total_sum -= heapq.heappop(heap)

            if len(heap) == k:
                max_score = max(max_score, total_sum * n2)

        return max_score


if __name__ == "__main__":
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    object = Solution3()
    print(f"Maximum subsequence Score :- {object.maxScore(nums1, nums2, k)}")
