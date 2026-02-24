from typing import List


class Solution2:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        def backtrack(start, remaining_k, remaining_sum, path):
            if remaining_k == 0 and remaining_sum == 0:
                result.append(path[:])
                return

            if remaining_k < 0 and remaining_sum < 0:
                return

            for num in range(start, 10):
                path.append(num)
                backtrack(num + 1, remaining_k - 1, remaining_sum - num, path)

                path.pop()

        backtrack(1, k, n, [])
        return result


if __name__ == "__main__":
    k, n = 3, 7
    object = Solution2()
    print(f"Comination Sum-III are - {object.combinationSum3(k, n)}")
