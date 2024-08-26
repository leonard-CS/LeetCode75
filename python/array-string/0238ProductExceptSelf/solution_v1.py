#2024.08.26
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        left = 1
        for i in range(n):
            prefix[i] = left
            left *= nums[i]

        right = 1
        for i in range(n-1, -1, -1):
            suffix[i] = right
            right *= nums[i]

        return [prefix[i] * suffix[i] for i in range(n)]


# nums   =     1,   2,   3,     4
# prefix =     1,   1, 1*2, 1*2*3
# suffix = 2*3*4, 3*4,   4,     1
# output =    24,  12,   8,     6
