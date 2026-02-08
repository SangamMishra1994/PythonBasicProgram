class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1

        return sp == len(s)


str1 = "abc"
str2 = "ahbgdc"

object = Solution2()
print(f"Result: - {object.isSubsequence(str1, str2)}")
