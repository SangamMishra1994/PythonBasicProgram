import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.current = 1  # Next natural number
        self.heap = []  # Min-heap for added back numbers
        self.added = set()  # To prevent duplicates in heap

    def popSmallest(self) -> int:
        # If heap has numbers, return smallest from heap
        if self.heap:
            smallest = heapq.heappop(self.heap)
            self.added.remove(smallest)
            return smallest

        # Otherwise return current number
        val = self.current
        self.current += 1
        return val

    def addBack(self, num: int) -> None:
        # Only add back if:
        # 1. num < current (meaning it was already popped)
        # 2. not already present in heap
        if num < self.current and num not in self.added:
            heapq.heappush(self.heap, num)
            self.added.add(num)


# Example usage (like LeetCode testing)
if __name__ == "__main__":
    obj = SmallestInfiniteSet()
    print(obj.popSmallest())  # 1
    print(obj.popSmallest())  # 2
    obj.addBack(1)
    print(obj.popSmallest())  # 1
    print(obj.popSmallest())  # 3
