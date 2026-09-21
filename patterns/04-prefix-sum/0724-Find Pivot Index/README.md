> 💡 **Note:** This problem is solved using the **Prefix Sum** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [0724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

Given an array of integers `nums`, calculate the **pivot index** of this array.

The **pivot index** is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is `0` because there are no elements to the left. This also applies to the right edge of the array.

Return the **leftmost pivot index**. If no such index exists, return `-1`.

### Example 1:
> **Input:** `nums = [1,7,3,6,5,6]`  
> **Output:** `3`  
> **Explanation:**  
> The pivot index is 3.  
> Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11  
> Right sum = nums[4] + nums[5] = 5 + 6 = 11  

### Example 2:
> **Input:** `nums = [1,2,3]`  
> **Output:** `-1`  
> **Explanation:**  
> There is no index that satisfies the conditions in the problem statement.  

---

### 1. Prefix Sum Math Trick Approach (Optimal)

Instead of calculating the left and right sums from scratch for every single index, we can use a basic mathematical deduction. We first calculate the total sum of the entire array.

**The Core Logic (The `val` trick):**
At any given index, the array is conceptually split into three parts:
1. Everything to the left (`left_sum`)
2. The current element itself (`val`)
3. Everything to the right (`right_sum`)

Therefore, the equation is: `total_sum = left_sum + val + right_sum`
By rearranging this equation, we can find the right side instantly without any loops:
`right_sum = total_sum - left_sum - val`

As we iterate through the array, we check if `left_sum == right_sum`. If they match, we've found our pivot. If not, we add the current `val` to our `left_sum` and move to the next index.

```python
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        
        for index, val in enumerate(nums):
            right_sum = total_sum - left_sum - val
            
            if left_sum == right_sum:
                return index
                
            left_sum += val
            
        return -1
```

**Time Complexity:** `O(N)`  
We iterate through the array twice: once to calculate the `total_sum` and once to find the pivot index. This is strictly linear time.

**Space Complexity:** `O(1)`  
We only use variables like `total_sum` and `left_sum`, requiring constant extra space.

--- 

### 2. Double While Loops Approach (Brute Force)

For every element in the array, we establish a left pointer and a right pointer. We use two separate `while` loops to calculate the sum strictly to the left and strictly to the right. If they match, we return the index. 

This recalculates overlapping parts of the array repeatedly, making it highly inefficient.

```python
class SolutionBruteForce:
    def pivotIndex(self, nums: list[int]) -> int:
        for index, val in enumerate(nums):
            left = 0
            right = len(nums) - 1
            left_sum = 0
            right_sum = 0
            
            while left < index:
                left_sum += nums[left]
                left += 1
                
            while index < right:
                right_sum += nums[right]
                right -= 1
                
            if right_sum == left_sum:
                return index
                
        return -1
```

**Time Complexity:** `O(N^2)`  
For each of the elements, we iterate through the rest of the array to calculate the sums, resulting in a quadratic time limit exceeded scenario for large inputs.

**Space Complexity:** `O(1)`  
We only track indices and running sums.