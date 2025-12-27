# 2402. Meeting Rooms III
# Hard

import collections
import heapq
from collections import deque
from sched import scheduler

"""
    if there is freeroom, and the start time of the meeting is less than the lowet endtime in scheduled heap:
        we pop free_room and add use the free room

    if no free room is available:
        we taken smalled ending time scheduled and add to that

    if no free room and smallest ending time > start_time, we delay the meeting
"""


def mostBooked(n: int, meetings: list[list[int]]) -> int:
    meetings.sort(key=lambda x: x[0])

    count = collections.defaultdict(int)

    free_rooms = list(range(n))
    scheduled = []

    for start_time, end_time in meetings:
        # clearing meetings, and freeing rooms first
        while scheduled and scheduled[0][0] <= start_time:
            _, room_id = heapq.heappop(scheduled)
            heapq.heappush(free_rooms, room_id)

        if free_rooms:
            room_id = heapq.heappop(free_rooms)
            heapq.heappush(scheduled, (end_time, room_id))
            count[room_id] += 1
        else:
            ending_time, room_id = heapq.heappop(scheduled)
            interval = end_time - start_time
            heapq.heappush(scheduled, (ending_time + interval, room_id))
            count[room_id] += 1

    max_count = 0
    room_id = 0

    for id, used in count.items():
        if used > max_count:
            max_count = used
            room_id = id

    print("Meetings  ", meetings)
    print("Free Rooms", free_rooms)
    print("Scheduled ", scheduled)
    print("Count     ", count)
    print("\n")

    return room_id


print(f"Example 1: {mostBooked(2, [[0, 10], [1, 5], [2, 7], [3, 4]])}")
print(f"Example 2: {mostBooked(3, [[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]])}")
print(f"Example 3: {mostBooked(2, [[0, 10], [1, 2], [12, 14], [13, 15]])}")
print(f"Example 4: {mostBooked(4, [[18, 19], [3, 12], [17, 19], [2, 13], [7, 10]])}")
print(
    f"Example 5: {mostBooked(4, [[48, 49], [22, 30], [13, 31], [31, 46], [37, 46], [32, 36], [25, 36], [49, 50], [24, 34], [6, 41]])}"
)
