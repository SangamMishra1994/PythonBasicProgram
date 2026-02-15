from typing import List


class Solution3:
    def findPeakElement(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return low


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    object = Solution3()
    print(f"Peak element index is :- {object.findPeakElement(nums)}")
