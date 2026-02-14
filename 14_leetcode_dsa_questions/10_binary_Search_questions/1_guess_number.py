# ----------------------------------
# Simulated guess API (Provided by LeetCode internally)
# ----------------------------------

# Let's assume the picked number is 6
picked_number = 5


def guess(num: int) -> int:
    if num > picked_number:
        return -1  # Too high
    elif num < picked_number:
        return 1  # Too low
    else:
        return 0  # Correct


# ----------------------------------
# Solution Class
# ----------------------------------


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n

        while left <= right:
            mid = left + (right - left) // 2
            result = guess(mid)

            if result == 0:
                return mid
            elif result == -1:
                right = mid - 1
            else:
                left = mid + 1

        return -1  # Just safety return


# ----------------------------------
# Driver Code
# ----------------------------------

if __name__ == "__main__":
    n = 10
    sol = Solution()
    answer = sol.guessNumber(n)
    print("Guessed Number:", answer)
