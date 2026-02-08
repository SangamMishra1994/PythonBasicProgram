class Solution1:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output_result = []
        # i, j = 0, 0

        # while i < len(word1) and j < len(word2):
        #     output_result.append(word1[i])
        #     output_result.append(word2[j])
        #     i += 1
        #     j += 1

        # if i < len(word1):
        #     output_result.append(word1[i:])

        # if j < len(word2):
        #     output_result.append(word2[j:])

        # return "".join(output_result)

        # Approach 2 using for loop
        min_len = min(len(word1), len(word2))
        for i in range(min_len):
            output_result.append(word1[i])
            output_result.append(word2[i])

        return "".join(output_result) + word1[min_len:] + word2[min_len:]


object = Solution1()
print(f'After Merging result = {object.mergeAlternately("abc", "pqr")}')
