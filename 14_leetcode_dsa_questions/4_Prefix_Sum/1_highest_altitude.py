from typing import List


class Solution1:
    def largestAltitude(self, gain: List[int]) -> int:
        current_altitude = 0
        max_altitude = 0

        for g in gain:
            # Prefix sum
            current_altitude += g
            max_altitude = max(max_altitude, current_altitude)

        return max_altitude


gain = [-5, 1, 5, 0, -7]
object = Solution1()
print(f"Highest Altitude : - {object.largestAltitude(gain)}")
