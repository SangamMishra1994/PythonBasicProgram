from typing import List


class Solution1:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(window_sum, max_sum)

        return max_sum / k


nums, k = [1, 12, -5, -6, 50, 3], 4
object = Solution1()
print(f"maximum average of subarray = {object.findMaxAverage(nums, k)}")
