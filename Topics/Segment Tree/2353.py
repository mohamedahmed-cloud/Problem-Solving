from typing import List
from collections import defaultdict
from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foodsRatings = defaultdict(str)
        self.couinsRatingsFoods = defaultdict(SortedSet)
        self.couinsFoods = defaultdict(str)
        self.n = len(foods)
        for i in range(self.n):
            self.foodsRatings[foods[i]] = ratings[i]
            self.couinsRatingsFoods[cuisines[i]].add((-ratings[i], foods[i]))
            self.couinsFoods[foods[i]] = cuisines[i]
        print(self.couinsRatingsFoods)

    def changeRating(self, food: str, newRating: int) -> None:
        oldRating = self.foodsRatings[food]
        cousines = self.couinsFoods[food]
        self.couinsRatingsFoods[cousines].remove((-oldRating, food))
        self.foodsRatings[food] = newRating
        self.couinsRatingsFoods[cousines].add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        print(self.couinsRatingsFoods)
        return self.couinsRatingsFoods[cuisine][0][1]

foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]
slv = FoodRatings(foods, cuisines, ratings)
print(slv.highestRated("korean"))
slv.changeRating("sushi", 16)
print(slv.highestRated("japanese"))




