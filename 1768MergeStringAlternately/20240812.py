import unittest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        for i in range(min(len(word1), len(word2))):
            result += word1[i] + word2[i]
        return result + word1[i+1:] + word2[i+1:]

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.mergeAlternately("abc", "pqr"), "apbqcr")
    
    def test_case2(self):
        self.assertEqual(self.sol.mergeAlternately("ab", "pqrs"), "apbqrs")
    
    def test_case3(self):
        self.assertEqual(self.sol.mergeAlternately("abcd", "pq"), "apbqcd")

if __name__ == '__main__':
    unittest.main()
