# 881. Boats to Save People
# Medium


def numRescueBoats(people: list[int], limit: int) -> int:
    # sorting
    people.sort()

    lo, hi = 0, len(people) - 1

    boats = 0

    while lo < hi:
        curr_weight = people[lo] + people[hi]
        if curr_weight <= limit:
            boats += 1
            lo += 1
            hi -= 1

        else:
            hi -= 1

    return boats + (len(people) - boats * 2)


people = [1, 2]
limit = 3
print(f"Example 1: {numRescueBoats(people, limit)}")

people = [3, 2, 2, 1]
limit = 3
print(f"Example 2: {numRescueBoats(people, limit)}")

people = [3, 5, 3, 4]
limit = 5
print(f"Example 2: {numRescueBoats(people, limit)}")
