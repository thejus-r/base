from typing import List
from sortedcontainers import SortedList
from collections import defaultdict

class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rankings = defaultdict(SortedList)
        self.lookup = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.rankings[c].add((-r, f))
            self.lookup[f] = (c, r)


    def changeRating(self, food: str, newRating: int) -> None:
        c, oldRating = self.lookup[food]
        self.lookup[food] = (c, newRating)
        self.rankings[c].remove((-oldRating, food))
        self.rankings[c].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.rankings[cuisine][0][1]

fr = FoodRatings(["kimchi","miso","sushi","moussaka","ramen","bulgogi"], ["korean","japanese","japanese","greek","japanese","korean"], [9,12,8,15,14,7])

print(fr.highestRated("korean"))