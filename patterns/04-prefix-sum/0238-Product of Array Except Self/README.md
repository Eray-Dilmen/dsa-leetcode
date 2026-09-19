> 💡 **Note:** This problem is solved using the **Prefix Sum** pattern (specifically tracking prefix and suffix products). For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in `O(N)` time and without using the division operation.

### Example 1:
> **Input:** `nums = [1,2,3,4]`  
> **Output:** `[24,12,8,6]`  

### Example 2:
> **Input:** `nums = [-1,1,0,-3,3]`  
> **Output:** `[0,0,9,0,0]`  

---

### 1. Prefix and Suffix Products Approach (Optimal)

To find the product of all elements except the current one without using division, we need to multiply all the elements to the *left* of the current index with all the elements to its *right*. 

**The Core Logic:**
* In the very first `for` loop, we traverse the array from left to right. We calculate the product of all elements to the left of each index and store these prefix products directly in our `ans` array. 
* In the subsequent `for` loop (which runs backwards), we calculate the running product from the right (`rightProduct`). We multiply this right-side product directly with the existing value in our `ans` array. 
* **Why does this work so perfectly?** Because the existing value in the left-side calculation was exactly the cumulative product of everything to its left up to that point! By multiplying this already-stored left product with our incoming right product, we successfully get the total product excluding the element itself, all while keeping space complexity strictly constant.

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        ans[0] = 1
        
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
            
        rightProduct = 1
        
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= rightProduct
            rightProduct *= nums[i]
            
        return ans
```

**Time Complexity:** `O(N)`

We iterate through the array exactly twice (once forward, once backward). The time complexity is strictly linear.

**Space Complexity:** `O(1)`

The problem description explicitly states that the output array `ans` does not count as extra space for space complexity analysis. We only use a single integer variable (`rightProduct`), meaning our extra space footprint is constant.

--- 

### 2. Nested For Loops Approach (Brute Force 1 - Time Limit Exceeded)

A straightforward brute force way is to use nested loops. For every element at index `i`, we iterate through the entire array again using an inner loop (`j`). If `i == j`, we use the `continue` statement to skip it. Otherwise, we multiply the numbers together. 

```python
class SolutionBruteForce1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            summ = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                summ *= nums[j]
                
            ans[i] = summ
            
        return ans
```

**Time Complexity:** `O(N^2)`

For each of the `N` elements, we scan the entire array of size `N` again. This quadratic time complexity results in a Time Limit Exceeded (TLE) error on LeetCode.

**Space Complexity:** `O(1)`

Excluding the output array, we only use a running product variable.

---

### 3. Two-Sided While Loops Approach (Brute Force 2 - Time Limit Exceeded)

This is a slightly more structured brute force approach. For each element at index `i`, we use two `while` loops. The first loop calculates the product of everything from the start up to `i-1` (the prefix). The second loop calculates the product of everything from the very end down to `i+1` (the suffix). 

Although conceptually separating the prefix and suffix logic is on the right track towards the optimal solution, doing it from scratch for *every single element* still takes too much time.

```python
class SolutionBruteForce2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        
        for i in range(len(nums)):
            prefix = 0
            summ = 1
            suffix = len(nums) - 1
            
            while prefix < i:
                summ *= nums[prefix]
                prefix += 1
                
            while suffix > i:
                summ *= nums[suffix]
                suffix -= 1
                
            ans[i] = summ
            
        return ans
```

**Time Complexity:** `O(N^2)`

Even though the work is split between two `while` loops, their combined iterations for each `i` still total `N-1` steps. Doing this `N` times makes it `O(N^2)`.

**Space Complexity:** `O(1)`

Only a few tracking variables are used.