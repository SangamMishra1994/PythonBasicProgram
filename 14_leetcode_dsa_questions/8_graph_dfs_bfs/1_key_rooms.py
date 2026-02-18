from typing import List


class Solution1:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()

        def dfs(room):
            if room in visited:
                return
            visited.add(room)

            for key in rooms[room]:
                dfs(key)

        dfs(0)

        return len(visited) == len(rooms)


if __name__ == "__main__":
    rooms = [[1], [2], [3], []]
    object = Solution1()
    print(f"All the rooms are visited? :- {object.canVisitAllRooms(rooms)}")
