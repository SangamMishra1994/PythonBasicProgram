from typing import List


class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        result = []

        def backtrack(index, path):
            if index == len(digits):
                result.append(path)
                return

            possible_letters = phone[digits[index]]

            for letter in possible_letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return result


if __name__ == "__main__":
    digits = "23"
    object = Solution1()
    print(f"Combination is : - {object.letterCombinations(digits)}")
