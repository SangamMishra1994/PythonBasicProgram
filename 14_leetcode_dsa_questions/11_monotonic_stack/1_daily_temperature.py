from typing import List


class Solution1:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)

        return answer


if __name__ == "__main__":
    temp = [73, 74, 75, 71, 69, 72, 76, 73]
    object = Solution1()
    print(f"Daily Temperature :- {object.dailyTemperatures(temp)}")
