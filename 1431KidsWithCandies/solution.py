from typing import List


def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
	maxCandies = max(candies)
	return [candy+extraCandies >= maxCandies for candy in candies]
