class Solution3:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                # get the substring from the stack
                substring = ""
                while stack[-1] != "[":
                    substring = stack.pop() + substring
                stack.pop()

                # Find digit
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * substring)

        return "".join(stack)


s = "3[a]2[bc]"
object = Solution3()
print(f"The final string result :- {object.decodeString(s)}")
