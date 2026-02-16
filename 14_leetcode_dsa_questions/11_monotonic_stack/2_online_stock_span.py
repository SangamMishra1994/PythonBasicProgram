class StockSpanner:

    def __init__(self):
        # stack will store tuples: (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        # Pop all smaller or equal prices and accumulate span
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        # Push current price with computed span
        self.stack.append((price, span))
        return span


# Driver code (for testing like LeetCode input)
if __name__ == "__main__":
    obj = StockSpanner()
    inputs = [100, 80, 60, 70, 60, 75, 85]

    for price in inputs:
        print(obj.next(price), end=" ")
