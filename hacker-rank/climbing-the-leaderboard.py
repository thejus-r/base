# Climbing the Leaderboard
# Medium

import heapq


class Leaderboard:
    def __init__(self, ranked: list[int]) -> None:
        self.data = []
        for score in ranked:
            self.add_score(score)

    def add_score(self, score: int) -> None:
        if -score not in self.data:
            heapq.heappush(self.data, -score)

    def get_rank(self, score: int) -> int:
        temp = self.data.copy()
        i = 1

        while temp:
            got_score = heapq.heappop(temp)
            if got_score == -score:
                break
            i += 1

        return i


def climbingLeaderboard(ranked: list[int], player: list[int]):
    res = []

    lb = Leaderboard(ranked)

    for score in player:
        lb.add_score(score)
        rank = lb.get_rank(score)
        res.append(rank)

    return res


print(f"Example 1: {climbingLeaderboard([100, 90, 90, 80], [70, 80, 105])}")
