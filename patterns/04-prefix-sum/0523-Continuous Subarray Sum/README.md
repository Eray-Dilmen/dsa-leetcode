> 💡 **Note:** This problem is solved using the **Prefix Sum** pattern (specifically combining it with Modulo Arithmetic and a Hash Map). For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [0523. Continuous Subarray Sum](https://leetcode.com/problems/continuous-subarray-sum/)

Given an integer array `nums` and an integer `k`, return `true` if `nums` has a **good subarray** or `false` otherwise.

A **good subarray** is a subarray where:
* its length is at least two, and
* the sum of the elements of the subarray is a multiple of `k`.

**Note that:**
* A subarray is a contiguous part of the array.
* An integer `x` is a multiple of `k` if there exists an integer `n` such that `x = n * k`. `0` is always a multiple of `k`.

### Example 1:
> **Input:** `nums = [23,2,4,6,7]`, `k = 6`  
> **Output:** `true`  
> **Explanation:** `[2, 4]` is a continuous subarray of size 2 whose elements sum up to 6.  

### Example 2:
> **Input:** `nums = [23,2,6,4,7]`, `k = 6`  
> **Output:** `true`  
> **Explanation:** `[23, 2, 6, 4, 7]` is an continuous subarray of size 5 whose elements sum up to 42. 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.  

### Example 3:
> **Input:** `nums = [23,2,6,4,7]`, `k = 13`  
> **Output:** `false`  

---

### 1. Prefix Sum with Hash Map & Modulo Approach (Optimal)

To determine if the sum of a contiguous subarray is a multiple of `k`, we can use the properties of modulo arithmetic. If `(prefix_sum_j - prefix_sum_i) % k == 0`, it implies that `prefix_sum_j % k == prefix_sum_i % k`. Therefore, we just need to keep track of the running sum's remainders when divided by `k`.

**The `{0: -1}` Initialization Detail:**
Why do we initialize our hash map with `{0: -1}`? This is a crucial step to handle valid subarrays that start exactly from the beginning of the array (index 0). 
If the first two elements sum up to a multiple of `k`, their remainder will be `0`. The current index would be `1`. Our length condition is `current_index - previous_index >= 2`. If we map the remainder `0` to the index `-1`, the calculation becomes `1 - (-1) = 2`, which correctly satisfies the length requirement of being at least 2.

```python
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_map = {0: -1}
        summ = 0
        
        for index, val in enumerate(nums):
            summ += val
            rem = summ % k
            
            if rem in remainder_map:
                if index - remainder_map[rem] >= 2:
                    return True
            else:
                remainder_map[rem] = index
                
        return False
```

**Time Complexity:** `O(N)`
We traverse the array `nums` exactly once. Dictionary lookups and insertions take `O(1)` time on average.

**Space Complexity:** `O(min(N, k))`
The hash map stores at most `N` remainders if the array is small, or at most `k` distinct remainders since any number modulo `k` has exactly `k` possible outcomes (from `0` to `k-1`).

--- 

### 2. Nested Loops Approach (Brute Force - Time Limit Exceeded)

This is a direct brute-force check. For every element at index `i`, we start an inner loop at `i+1` to expand the subarray to the right. We continuously add the elements to our running `summ`. Because the inner loop starts at `i+1`, the subarray length is inherently at least 2. If at any point the `summ % k == 0`, we immediately return `True`.

```python
class SolutionBruteForce:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        for i in range(0, len(nums)-1):
            summ = nums[i]
            for j in range(i+1, len(nums)):
                summ += nums[j]
                if summ % k == 0:
                    return True
                    
        return False
```

**Time Complexity:** `O(N^2)`
For each element, we potentially scan the rest of the array. In the worst case, this results in quadratic time complexity, causing a Time Limit Exceeded on large test cases.

**Space Complexity:** `O(1)`
We are only maintaining a single `summ` variable to track the running sum.