import unittest
from solution_v1 import Solution

class TestSolutionV1(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.canPlaceFlowers([1, 0, 0, 0, 1], 1), True)
    
    def test_case2(self):
        self.assertEqual(self.sol.canPlaceFlowers([1, 0, 0, 0, 1], 2), False)

    def test_case3(self):
        self.assertEqual(self.sol.canPlaceFlowers([0, 0, 0, 0], 2) , True)

    def test_case4(self):
        self.assertEqual(self.sol.canPlaceFlowers([0, 0, 0, 0], 3) , False)

    def test_case5(self):
        self.assertEqual(self.sol.canPlaceFlowers([1, 0, 1, 0, 1, 0, 1], 0) , True)

if __name__ == '__main__':
    unittest.main()
