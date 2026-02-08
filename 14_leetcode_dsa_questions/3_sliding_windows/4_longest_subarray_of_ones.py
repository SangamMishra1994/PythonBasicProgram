from typing import List


class Solution4:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_window = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_window = max(max_window, right - left + 1)

        return max_window - 1


nums = [1, 1, 0, 1, 1]
object = Solution4()
print(f"Final answer : - {object.longestSubarray(nums)}")
