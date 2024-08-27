# Notes for Problem 334
- **Title**: [334. Increasing Triplet Subsequence](https://leetcode.com/problems/increasing-triplet-subsequence/description/)
- **Description**: Given an integer array `nums`, return `true` if there exists a triple of indices `(i, j, k)` such that `i < j < k` and `nums[i] < nums[j] < nums[k]`. If no such indices exists, return `false`.

# Hint
So we need to see if there is an increasing triplet. Now if there is one such triplet, the smallest number in the triplet can be replaced by the smallest number in the whole array up to the index of the number in the middle of the triplet. (Sorry for the loaded sentence)

Observing this fact, we can walk the array, track the minimum number so far (call it A). On top of that, we also track the smallest number that is bigger than A and is to the right of A (call it B). As long as we do that, then once we see a third number that is bigger than B, we can return true.

# Approach and Solutions

## Approach 1:
- **Description**: Follow the hint
- **Complexity**:
    - **Time Complexity**: O(n), where n is the length of the list.
    - **Space Complexity**: O(1)
- **Code**: [solution_v1.py](solution_v1.py)
    - Explantion of the usage of `<=`:
        This ensure `first` always holds the smallest possible value seen so far and `second` holds the smallest value that is larger than `first`. (see [test case 5](test_solution.py))