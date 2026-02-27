from typing import List


class Solution3:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        dp = [0] * n

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return dp[-1]


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    object = Solution3()
    print(f"Total amount you can rob = {object.rob(nums)}")
