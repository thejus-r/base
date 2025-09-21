from typing import List
from sortedcontainers import SortedSet
from collections import defaultdict
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.available_movies = defaultdict(SortedSet)
        self.movie_price = {}
        self.rented_movies = SortedSet()

        for shop, movie, price in entries:
            self.available_movies[movie].add((price, shop))
            self.movie_price[(movie, shop)] = price

    def search(self, movie: int) -> List[int]:
        top_shops = []

        for _, shop in self.available_movies[movie]:
            top_shops.append(shop)
            if len(top_shops) == 5:
                break
        return top_shops


    def rent(self, shop: int, movie: int) -> None:
        price = self.movie_price[(movie, shop)]
        self.rented_movies.add((price, shop, movie))
        self.available_movies[movie].discard((price, shop))

    def drop(self, shop: int, movie: int) -> None:
        price = self.movie_price[(movie, shop)]
        self.rented_movies.discard((price, shop, movie))
        self.available_movies[movie].add((price, shop))


    def report(self) -> List[List[int]]:
        top_rented = []
        for price, shop, movie in self.rented_movies:
            top_rented.append([shop, movie])
            if len(top_rented) == 5:
                break
        return top_rented
