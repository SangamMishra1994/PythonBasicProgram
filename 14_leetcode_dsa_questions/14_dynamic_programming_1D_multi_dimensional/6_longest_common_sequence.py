class Solution6:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * len(text1)
        longest = 0

        for c in text2:
            cur_length = 0
            for i, val in enumerate(dp):
                if cur_length < val:
                    cur_length = val
                elif c == text1[i]:
                    dp[i] = cur_length + 1
                    longest = max(longest, cur_length + 1)

        return longest


if __name__ == "__main__":
    text1, text2 = "abcde", "ace"
    object = Solution6()
    print(f"Longest common sequence ->"
          f"{object.longestCommonSubsequence(text1, text2)}")
