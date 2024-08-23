# Notes for Problem 605

## Problem Statement
- **Title**: [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/description/)
- **Description**: You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

## Hint
- We do not want any flower beds one place ahead of our current index and one place behind our index. So check for that while traversing the array.

## Approach and Solutions

### Approach 1:
- **Description**: Traverse the flowerbed from left to right. For each plot, check if it and its adjacent plots are empty. If so, plant a flower and continue.
- **Complexity**:
    - **Time Complexity**: O(m), where m is the length of the flowerbed.
    - **Space Complexity**: O(1)
- **Code**: [solution_v1.py](solution_v1.py)

## Edge Cases
- **Case 1**: Check if the first and last plots are handled correctly. They don't have both left and right neighbors.
- **Case 2**: If `n`is zero, the function should return `True` immediately as no flowers need to be planted.
