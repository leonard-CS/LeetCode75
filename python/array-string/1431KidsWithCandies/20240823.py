import unittest
from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return list(map(lambda x: x + extraCandies >= maxCandies, candies))

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.kidsWithCandies([2, 3, 5, 1, 3], 3), [True, True, True, False, True])
    
    def test_case2(self):
        self.assertEqual(self.sol.kidsWithCandies([4, 2, 1, 1, 2], 1), [True, False, False, False, False])
    
    def test_case3(self):
        self.assertEqual(self.sol.kidsWithCandies([12, 1, 12], 10), [True, False, True])

if __name__ == '__main__':
    unittest.main()
    