import heapq
from typing import List


class Solution4:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        n = len(costs)

        # Edge case
        if 2 * candidates >= n:
            return sum(sorted(costs)[:k])

        left_heap = []
        right_heap = []

        left = 0
        right = n - 1

        # Initialize heaps
        for _ in range(candidates):
            heapq.heappush(left_heap, costs[left])
            left += 1

        for _ in range(candidates):
            heapq.heappush(right_heap, costs[right])
            right -= 1

        total_cost = 0

        for _ in range(k):

            # If right heap empty OR left smallest <= right smallest
            if not right_heap or (left_heap and left_heap[0] <= right_heap[0]):
                total_cost += heapq.heappop(left_heap)

                if left <= right:
                    heapq.heappush(left_heap, costs[left])
                    left += 1
            else:
                total_cost += heapq.heappop(right_heap)

                if left <= right:
                    heapq.heappush(right_heap, costs[right])
                    right -= 1

        return total_cost


if __name__ == "__main__":
    costs = [17, 12, 10, 2, 7, 2, 11, 20, 8]
    k = 3
    candidates = 4
    object = Solution4()
    print(f"Total costs for hire the {candidates} worker is :- "
          f"{object.totalCost(costs, k, candidates)}")
