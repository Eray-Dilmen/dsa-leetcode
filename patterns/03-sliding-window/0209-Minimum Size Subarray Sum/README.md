> 💡 **Note:** This problem is solved using the **Sliding Window** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/)

**Problem Statement**
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0` instead.

### Example 1:
> **Input:** `target = 7, nums = [2,3,1,2,4,3]`
> **Output:** `2`
> **Explanation:** The subarray `[4,3]` has the minimal length under the problem constraint.

### Example 2:
> **Input:** `target = 4, nums = [1,4,4]`
> **Output:** `1`

### Example 3:
> **Input:** `target = 11, nums = [1,1,1,1,1,1,1,1]`
> **Output:** `0`

---

### 1. Sliding Window Approach (Optimal)

We use a sliding window defined by two pointers, `l` (left) and `r` (right). As we iterate through the array with our right pointer `r`, we continuously add the current element to a running total (`summ`). 

Because all numbers in the array are positive, we know that adding more elements will only increase the sum. Once our `summ` becomes greater than or equal to the `target`, our current window is valid. We then try to shrink this valid window from the left to find the strictly minimum length. We do this by updating our minimum length variable (`minn`), subtracting the element at the left pointer (`nums[l]`) from our sum, and incrementing `l`. We repeat this shrinking process as long as the window's sum remains valid.

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        minn = float('inf')
        summ = 0
        l = 0
        
        for r in range(len(nums)):
            summ += nums[r]
            
            while summ >= target:
                minn = min(minn, r - l + 1)
                summ -= nums[l]
                l += 1
                
        return minn if minn != float('inf') else 0
```

--- 

### 2. Nested Loops Approach (Brute Force)

We can check all possible subarrays using two nested loops. The outer loop selects the starting index, and the inner loop expands the subarray to the right, maintaining a running sum. As soon as the sum reaches or exceeds the `target`, we record the length, break the inner loop (since any further expansion would only increase the length unnecessarily due to positive integers), and move to the next starting index.

```python
class SolutionBruteForce:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)
        minn = float('inf')
        n = len(nums)
        
        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += nums[j]
                if summ >= target:
                    minn = min(minn, j - i + 1)
                    break
                    
        return minn if minn != float('inf') else 0
```