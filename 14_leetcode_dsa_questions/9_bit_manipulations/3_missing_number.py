from typing import List


class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        result = n

        for i in range(n):
            result ^= i ^ nums[i]

        return result


if __name__ == "__main__":
    nums = [3, 0, 1]
    object = Solution3()
    print(f"Missing number is :- {object.missingNumber(nums)}")
