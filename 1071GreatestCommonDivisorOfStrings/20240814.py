import unittest


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd_value = self.gcd(len(str1), len(str2))
        result = str1[:gcd_value]
        flag1, flag2 = True, True
        for j in range(0, len(str1), gcd_value):
            if str1[j:j+gcd_value] != result:
                flag1 = False
        for j in range(0, len(str2), gcd_value):
            if str2[j:j+gcd_value] != result:
                flag2 = False
        if flag1 and flag2:
            return result
        return ""
    
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a
    
    # def find_common_divisors(self, a, b):
    #     gcd_value = self.gcd(a, b)
    #     common_divisors = [gcd_value]
    #     for i in range(gcd_value - 1, 0, -1):
    #         if gcd_value % i == 0:
    #             common_divisors.append(i)
    #     print(common_divisors)
    #     return common_divisors
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.gcdOfStrings("ABCABC", "ABC"), "ABC")
    
    def test_case2(self):
        self.assertEqual(self.sol.gcdOfStrings("ABABAB", "ABAB"), "AB")
    
    def test_case3(self):
        self.assertEqual(self.sol.gcdOfStrings("LEET", "CODE"), "")

if __name__ == '__main__':
    unittest.main()