class Solution3:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Approch 1, using brute force
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in word1:
            freq1[ord(ch) - ord("a")] += 1

        for ch in word2:
            freq2[ord(ch) - ord("a")] += 1

        for i in range(26):
            if ((freq1[i] == 0 and freq2[i] != 0) or
                    (freq2[i] == 0 and freq1[i] != 0)):
                return False

        freq1.sort()
        freq2.sort()

        for i in range(26):
            if freq1[i] != freq2[i]:
                return False

        return True

        # Approach 2:- Using Counter() method
        # freq_word1 = Counter(word1)
        # freq_word2 = Counter(word2)

        # sorted_values_word1 = sorted(freq_word1.values())
        # sorted_values_word2 = sorted(freq_word2.values())

        # keys_match = set(freq_word1.keys()) == set(freq_word2.keys())
        # return sorted_values_word1 == sorted_values_word2 and keys_match


word1 = "abc"
word2 = "bca"

object = Solution3()
print(f"Are two string are equal :- {object.closeStrings(word1, word2)}")
