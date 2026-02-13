from typing import List


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result


if __name__ == "__main__":
    nums = [4, 1, 2, 1, 2]

    object = Solution2()
    print(f"Single Number is : {object.singleNumber(nums)}")
