# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u',
# and they can appear in both lower and upper cases, more than once


class Solution5:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s_list = list(s)

        left = 0
        right = len(s) - 1
        while left < right:
            if s_list[left] in vowels and s_list[right] in vowels:
                s_list[left], s_list[right] = s_list[right], s_list[left]
                left += 1
                right -= 1
            elif s_list[right] not in vowels:
                right -= 1
            elif s_list[left] not in vowels:
                left += 1
        return "".join(s_list)


s = "IceCreAm"
object = Solution5()
print(f"Output will be = {object.reverseVowels(s)}")
