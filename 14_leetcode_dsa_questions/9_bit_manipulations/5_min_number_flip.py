class Solution5:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flip = 0

        for i in range(32):
            a_bit = (a >> i) & 1
            b_bit = (b >> i) & 1
            c_bit = (c >> i) & 1

            if c_bit == 1:
                if a_bit == 0 and b_bit == 0:
                    flip += 1

            else:
                if a_bit == 1:
                    flip += 1
                if b_bit == 1:
                    flip += 1

        return flip


if __name__ == "__main__":
    object = Solution5()
    print(f"Minimum number of flip : - {object.minFlips(2, 6, 5)}")
