# 3433. Count Mentions Per User
# Medium


def countMentions(numberOfUsers: int, events: list[list[str]]) -> list[int]:
    events.sort(key=lambda x: (int(x[1]), x[0] == "MESSAGE"))

    print("sorted: ", events)

    count = [0] * numberOfUsers
    next_online_time = [0] * numberOfUsers

    for event in events:
        curr_time = int(event[1])
        if event[0] == "MESSAGE":
            if event[2] == "ALL":
                for i in range(numberOfUsers):
                    count[i] += 1
            elif event[2] == "HERE":
                for i, t in enumerate(next_online_time):
                    if t <= curr_time:
                        count[i] += 1
            else:
                for idx in event[2].split():
                    count[int(idx[2:])] += 1
        else:
            next_online_time[int(event[2])] = curr_time + 60

    return count


events = [
    ["MESSAGE", "10", "id1 id0"],
    ["OFFLINE", "11", "0"],
    ["MESSAGE", "12", "ALL"],
]
numberOfUsers = 2

print(f"Example 1: {countMentions(numberOfUsers, events)}")

events = [["OFFLINE", "10", "0"], ["MESSAGE", "12", "HERE"]]
numberOfUsers = 2
print(f"Example 2: {countMentions(numberOfUsers, events)}")


events = [
    ["MESSAGE", "2", "HERE"],
    ["OFFLINE", "2", "1"],
    ["OFFLINE", "1", "0"],
    ["MESSAGE", "61", "HERE"],
]
numberOfUsers = 3
print(f"Example 3: {countMentions(numberOfUsers, events)}")


events = [
    ["MESSAGE", "5", "HERE"],
    ["OFFLINE", "10", "0"],
    ["MESSAGE", "15", "HERE"],
    ["OFFLINE", "18", "2"],
    ["MESSAGE", "20", "HERE"],
]
numberOfUsers = 3
print(f"Example 4: {countMentions(numberOfUsers, events)}")
