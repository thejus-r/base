# 1732. Find the Highest Altitude
# Easy
def largestAltitude(gain: list[int]) -> int:
    max_altitude = cur_altitude = 0

    for g in gain:
        cur_altitude += g
        max_altitude = max(max_altitude, cur_altitude)

    return int(max_altitude)


print("Example 1: ", largestAltitude([-5, 1, 5, 0, -7]))  # 1
print("Example 2: ", largestAltitude([-4, -3, -2, -1, 4, 3, 2]))  # 0
