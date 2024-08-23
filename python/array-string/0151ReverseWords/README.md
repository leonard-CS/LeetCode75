# Notes for Problem 151

## Problem Statement
- **Title**: [151. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/description/)
- **Description**: Given an input string `s`, reverse the order of the **words**.

## Approach and Solutions

### Approach 1:
- **Description**: Split the input string s into a list of words, reverse the order of the words, and then join them back into a single string with spaces in between.
- **Complexity**:
    - **Time Complexity**: O(m), where `m` is the length of the input string.
    - **Space Complexity**: O(n), where `n` is the number of words in the string.
- **Code**: [solution_v1.py](solution_v1.py)
    ```python
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
    ```
    - **Details**:
        - `[::-1]`: Reverses the list of words.
        - `' '.join(...)`: Joins the reversed list into a single string with words separated by a single space.
        