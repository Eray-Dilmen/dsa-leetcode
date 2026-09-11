> 💡 **Note:** This problem is solved using the **Sliding Window** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [1004. Max Consecutive Ones III](https://leetcode.com/problems/max-consecutive-ones-iii/)

**Problem Statement**
Given a binary array `nums` and an integer `k`, return the maximum number of consecutive `1`'s in the array if you can flip at most `k` `0`'s.

### Example 1:
> **Input:** `nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2`  
> **Output:** `6`  
> **Explanation:** `[1,1,1,0,0,1,1,1,1,1,1]` 
> Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

### Example 2:
> **Input:** `nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3`  
> **Output:** `10`  
> **Explanation:** `[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]` 
> Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

---

### 1. Sliding Window Approach (Optimal)

We use a sliding window defined by two pointers, `l` (left) and `r` (right). We expand the window by moving `r` to the right. If we encounter a `0`, we increment our `num_zeros` count. When `num_zeros` exceeds `k`, the window becomes invalid, so we shrink it by moving `l` to the right until we drop a `0` out of the window. We constantly update the maximum window size.

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        max_w = 0
        num_zeros = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            w = r - l + 1
            max_w = max(max_w, w)

        return max_w
```

--- 

### 2. Nested Loops Approach (Brute Force)

We can check every possible subarray starting from each index. For each starting index, we expand a subarray and count the zeros. If the zero count exceeds `k`, we break and move to the next starting index. This results in a quadratic time complexity.

```python
class SolutionBruteForce:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)
        max_w = 0
        n = len(nums)

        for i in range(n):
            num_zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    num_zeros += 1
                if num_zeros > k:
                    break
                max_w = max(max_w, j - i + 1)
                
        return max_w
```