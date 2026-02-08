from typing import List


class Solution1:
    def findDifference(self, nums1: List[int], nums2: List[int]):
        set1 = set(nums1)
        set2 = set(nums2)

        only_in_num1 = list(set1 - set2)
        only_in_num2 = list(set2 - set1)

        return [only_in_num1, only_in_num2]


nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
object = Solution1()

print(f"Difference - {object.findDifference(nums1, nums2)}")
