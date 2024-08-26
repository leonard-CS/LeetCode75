import unittest
from solution_v1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        input_data = [1,2,3,4]
        expected_output = [24,12,8,6]
        self.assertEqual(self.sol.productExceptSelf(input_data), expected_output)

    def test_case_2(self):
        input_data = [-1,1,0,-3,3]
        expected_output = [0,0,9,0,0]
        self.assertEqual(self.sol.productExceptSelf(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
