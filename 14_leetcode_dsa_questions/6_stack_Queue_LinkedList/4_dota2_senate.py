from collections import deque


class Solution4:
    def predictPartyVictory(self, senate: str) -> str:
        r_deque = deque()
        d_deque = deque()
        n = len(senate)

        for index, value in enumerate(senate):
            if value == "R":
                r_deque.append(index)
            else:
                d_deque.append(index)

        while r_deque and d_deque:
            r = r_deque.popleft()
            d = d_deque.popleft()

            if r < d:
                r_deque.append(r + n)
            else:
                d_deque.append(d + n)

        return "Radiant" if r_deque else "Dire"


senate = "RD"
object = Solution4()
print(f"Winner is :- {object.predictPartyVictory(senate)}")
