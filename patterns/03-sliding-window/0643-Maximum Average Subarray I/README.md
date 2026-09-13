> 💡 **Note:** This problem is solved using the **Sliding Window** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/)

You are given an integer array `nums` consisting of `n` elements, and an integer `k`.
Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value. Any answer with a calculation error less than 10^-5 will be accepted.

### Example 1:
> **Input:** `nums = [1,12,-5,-6,50,3]`, `k = 4`  
> **Output:** `12.75000`  
> **Explanation:** Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

### Example 2:
> **Input:** `nums = [5]`, `k = 1`  
> **Output:** `5.00000`  

---

> 🧠 **Why do we use `float('-inf')` or `float('inf')`?**
> * **When searching for a Maximum (`max`):** You must set your initial starting bar to the lowest possible number (`-inf`). This ensures that the very first valid calculated value will easily surpass it and become the new maximum. If you used `+inf`, no number in the universe could beat it, and your answer would incorrectly remain `inf`.
> * **When searching for a Minimum (`min`):** You must set the bar to the highest possible number (`+inf`) so that any incoming value will be smaller and update it.

---

### 1. Fixed-Size Sliding Window Approach (Optimal)

* Since we are looking for a subarray of an exact length `k`, we can use a **Fixed-Size Sliding Window**. 
* We use a `for` loop to act as our right pointer (`r`), continuously adding elements to our current sum (`summ`).
* Once our window reaches the required size `k` (which happens when `(r - l + 1) == k`), we calculate the average and update our `max_avg`.
* To slide the window forward, we subtract the element at the left pointer (`nums[l]`) from our sum and increment `l`. This keeps the window size perfectly at `k` for the next iterations.

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        # Initialize to negative infinity so any valid average will surpass it
        max_avg = float('-inf') 
        summ = 0
        
        for r in range(len(nums)):
            summ += nums[r]
            
            if (r - l + 1) == k:
                avg = summ / k
                max_avg = max(max_avg, avg)
                summ -= nums[l]
                l += 1
                
        return max_avg
```

**Time Complexity:** `O(N)`

The right pointer iterates through the array exactly once. The left pointer also moves forward smoothly without going backward.

**Space Complexity:** `O(1)`

We only use a few variables (`l`, `max_avg`, `summ`, `avg`) which require constant extra space.

--- 

### 2. Nested Loops Approach (Brute Force)

* We can evaluate every possible subarray of length `k` by using a loop to mark the starting index and a nested loop (or array slicing) to calculate the sum of the `k` elements following it.
* While this logically works, it recalculates the overlapping parts of the subarrays repeatedly, making it extremely inefficient for large arrays.

```python
class SolutionBruteForce:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = float('-inf')
        n = len(nums)
        
        for i in range(n - k + 1):
            summ = sum(nums[i:i+k])
            avg = summ / k
            max_avg = max(max_avg, avg)
            
        return max_avg
```

**Time Complexity:** `O(N * K)`

For every element in the array, we iterate `k` times to calculate the sum, leading to a much slower execution time.

**Space Complexity:** `O(1)`

No extra data structures are used.