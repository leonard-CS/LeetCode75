import unittest
from solution_v1 import Solution

class TestSolutionV1(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.reverseWords("the sky is blue"), "blue is sky the")
    
    def test_case2(self):
        self.assertEqual(self.sol.reverseWords("  hello world  "), "world hello")

    def test_case3(self):
        self.assertEqual(self.sol.reverseWords("a good   example"), "example good a")

if __name__ == '__main__':
    unittest.main()
