class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        # Use of Manual Euclidean Algorithm (Mathematical)
        def get_gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        max_length = get_gcd(len(str1), len(str2))
        return str1[:max_length]

    #  Another approch using the gcd() method present in math library
    # max_length = gcd(len(str1), len(str2))
    # return str1[:max_length]


object = Solution2()
print(f'Final result is {object.gcdOfStrings("ABCABC", "ABC")}')
