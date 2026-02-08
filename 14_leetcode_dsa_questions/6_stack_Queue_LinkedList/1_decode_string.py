class Solution1:
    def removeStars(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == "*" and stack:
                stack.pop()
            else:
                stack.append(ch)

        return "".join(stack)


s = "leet**cod*e"
object = Solution1()
print(f"The final string is :- {object.removeStars(s)}")
