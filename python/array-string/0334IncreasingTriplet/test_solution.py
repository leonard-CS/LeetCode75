import unittest
from solution_v1 import Solution


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        input_data = [1,2,3,4,5]
        expected_output = True
        self.assertEqual(self.sol.increasingTriplet(input_data), expected_output)

    def test_case_2(self):
        input_data = [5,4,3,2,1]
        expected_output = False
        self.assertEqual(self.sol.increasingTriplet(input_data), expected_output)
    
    def test_case_3(self):
        input_data = [2,1,5,0,4,6]
        expected_output = True
        self.assertEqual(self.sol.increasingTriplet(input_data), expected_output)
    
    def test_case_4(self):
        input_data = [20,100,10,12,5,13]
        expected_output = True
        self.assertEqual(self.sol.increasingTriplet(input_data), expected_output)
    
    def test_case_5(self):
        input_data = [1,1,1]
        expected_output = False
        self.assertEqual(self.sol.increasingTriplet(input_data), expected_output)

if __name__ == '__main__':
    unittest.main()
