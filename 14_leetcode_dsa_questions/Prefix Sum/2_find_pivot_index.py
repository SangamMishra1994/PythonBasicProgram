from typing import List


class Solution2:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for index, num in enumerate(nums):
            right_sum -= num

            if left_sum == right_sum:
                return index
            left_sum += num
        return -1


nums = [1, 7, 3, 6, 5, 6]
object = Solution2()
print(f"Pivot index value : - {object.pivotIndex(nums)}")
