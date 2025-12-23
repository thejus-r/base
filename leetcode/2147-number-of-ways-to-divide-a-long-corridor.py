# 2147. Number of Ways to Divide a Long Corridor
# Hard


"""
Intuition:
    We can ignore all the beginning plants.

    We take all the plants between each segments.

    Edge Cases:
        - the corridor has, odd number of seats 'S', its not possible to divide
        - the corridor has no seats, so its not possible to divide
        - we return 0 in both cases.

"""


def numberOfWays(corridor: str) -> int:
    # odd number of seats

    if "S" not in corridor:
        return 0

    if corridor.count("S") % 2 != 0:
        return 0

    mod = 10**9 + 7
    INF = 10**20

    current_plants = -INF
    current_seats = 0
    count = 1
    for c in corridor:
        if c == "S":
            current_seats += 1

            if current_seats == 2:
                current_seats = 0
                current_plants = 0
            else:
                if current_plants >= 0:
                    count *= current_plants + 1
                    count %= mod

        else:
            current_plants += 1

    return count % mod


print("Example 1: ", numberOfWays("SSPPSPS"))
print("Example 2: ", numberOfWays("PPSPSP"))
print("Example 3: ", numberOfWays("S"))
