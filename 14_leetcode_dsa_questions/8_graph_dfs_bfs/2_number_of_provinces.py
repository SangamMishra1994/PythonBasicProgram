from typing import List


class Solution2:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        provinces = 0

        def dfs_helper(city):
            for neighbor in range(n):
                if (
                    isConnected[city][neighbor] == 1 and
                    neighbor not in visited
                ):
                    visited.add(neighbor)
                    dfs_helper(neighbor)

        for city in range(n):
            if city not in visited:
                visited.add(city)
                dfs_helper(city)
                provinces += 1

        return provinces


if __name__ == "__main__":
    isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    object = Solution2()
    print(f"Total No. of Provinces :- {object.findCircleNum(isConnected)}")
