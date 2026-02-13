from typing import List


class Solution1:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)

        for i in range(1, n + 1):

            # Approach - “For each number, I use DP where
            # ans[i] = ans[i >> 1] + (i & 1). Right shifting removes t
            # he last bit, and i & 1 checks if the last bit is set.
            # This gives O(n) time.”

            # i >> 1 → remove last bit (divide by 2)
            # (i & 1) → check if last bit is 1
            ans[i] = ans[i >> 1] + (i & 1)
        return ans


if __name__ == "__main__":
    n = 5
    object = Solution1()
    print(f"Counting Bits from 0 to , {n} :, {object.countBits(n)}")
