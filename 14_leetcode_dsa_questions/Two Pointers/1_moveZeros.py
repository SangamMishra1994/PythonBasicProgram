from typing import List


class Solution1:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1


array = [0, 1, 0, 3, 12]
object = Solution1()
print(f"Result: - {object.moveZeroes(array)}")
