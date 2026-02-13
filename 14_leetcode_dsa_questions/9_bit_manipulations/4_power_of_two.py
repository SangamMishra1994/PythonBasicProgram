class Solution4:
    def powerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0


if __name__ == "__main__":

    n = int(input("Enter the numer:- "))
    object = Solution4()
    print(f"Is {n} is power of 2:- {object.powerOfTwo(n)}")
