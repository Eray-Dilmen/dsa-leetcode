> 💡 **Note:** This problem is solved using the **Prefix Sum** pattern combined with a Hash Map. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
A subarray is a contiguous non-empty sequence of elements within an array.

### Example 1:
> **Input:** `nums = [1,1,1]`, `k = 2`  
> **Output:** `2`  

### Example 2:
> **Input:** `nums = [1,2,3]`, `k = 3`  
> **Output:** `2`  

---

### 1. Prefix Sum + Hash Map Approach (Optimal)

Instead of calculating the sum of every possible subarray from scratch, we keep a running cumulative sum (`prefix_sum`). As we iterate through the array, we use a hash map (`freq`) to store how many times each cumulative sum has occurred. 

**The Core Logic & "Why"s:**
* **Mathematical Logic:** Mathematically, the sum of a subarray is the difference between the cumulative sum at the end point and the cumulative sum just before the start point:  
  `Current_Prefix_Sum - Past_Prefix_Sum = k`  
  Rearranging this equation to match the code's perspective:  
  `Past_Prefix_Sum = Current_Prefix_Sum - k`  
  If we are at some current sum and want to find a subarray that sums to `k` ending at our current position, we are essentially looking for a past sum that we can cut off from the beginning. By checking if `prefix_sum - k` exists in our hash map, we instantly know if there is a valid subarray ending here.
* **Why start with `freq = {0: 1}`?:** This is our base case. It represents the state before we even start iterating: "The sum is 0 before any elements are picked." If our very first element equals `k` (e.g., element is 3, `k = 3`), the formula looks for `3 - 3 = 0`. Without `{0: 1}`, we would completely miss valid subarrays that start from the very first index (index 0).
* **Why add frequency (`count += freq[...]`) instead of just `+1`?:** The `prefix_sum - k` value is the part we are *cutting off* from the beginning of the array to leave a subarray of sum `k`. Because arrays can contain zeroes or negative numbers, the cumulative sum can fluctuate, meaning we might have hit that exact same *past sum* multiple times. Each time we hit it represents a completely different index where we can make a valid cut. Therefore, we must add the total number of times that cut-off sum occurred in the past.

```python
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0: 1}
        
        for num in nums:
            prefix_sum += num
            
            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]
                
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
            
        return count
```

**Time Complexity:** `O(N)`

We iterate through the array exactly once. Hash map insertions and lookups take `O(1)` time on average, resulting in a strictly linear time complexity.

**Space Complexity:** `O(N)`

In the worst-case scenario (e.g., all positive numbers), every `prefix_sum` will be unique, meaning we will store `N` distinct key-value pairs in the hash map.

--- 

### 2. Nested Loops Approach (Brute Force - Time Limit Exceeded)

We can systematically check every possible subarray by using two nested loops. The outer loop `l` defines the starting point of the subarray, and the inner loop `r` expands the subarray one element at a time, keeping a running sum. Whenever the running sum hits `k`, we increment our counter. 

While logically correct, this approach explores all $O(N^2)$ possible subarrays, which results in a **Time Limit Exceeded (TLE)** error for large inputs.

```python
class SolutionBruteForce:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        for l in range(len(nums)):
            summ = 0
            for r in range(l, len(nums)):
                summ += nums[r]
                if summ == k:
                    count += 1
        return count
```

**Time Complexity:** `O(N^2)`

The nested loops result in a quadratic time complexity as we evaluate the sum of every possible contiguous subarray.

**Space Complexity:** `O(1)`

We only use a few integer variables (`count`, `summ`) for tracking, requiring no extra memory.