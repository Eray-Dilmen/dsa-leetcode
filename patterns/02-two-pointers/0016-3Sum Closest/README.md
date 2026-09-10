> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/)

**Problem Statement**
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

### Example 1:
> **Input:** `nums = [-1,2,1,-4], target = 1`  
  **Output:** `2`  
  **Explanation:** The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

### Example 2:
> **Input:** `nums = [0,0,0], target = 1`  
  **Output:** `0`  

---

### 1. Sorting & Two Pointers Approach (Optimal)

This approach is highly similar to the standard 3Sum problem. By sorting the array first, we can iterate through the array and fix one number at a time (`nums[i]`). Then, we use the Two Pointers technique (`lo` and `hi`) on the remaining portion of the array to find the other two numbers. 

Instead of looking for an exact match, we track the `closest_sum` by comparing the absolute difference between the current sum and the target `abs(cur_sum - target)`. If the current sum perfectly matches the target, we return it immediately. Otherwise, we adjust the pointers based on whether the sum is too small or too large.

```python
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            lo, hi = i + 1, n - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]
                
                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum
                    
                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1
                    
        return closest_sum
```

**Time Complexity:** $O(N^2)$
Sorting the array takes $O(N \log N)$. The outer loop runs $O(N)$ times, and the inner Two Pointers loop takes $O(N)$ time. The total time complexity is bounded by $O(N^2)$.
**Space Complexity:** $O(1)$
We only use a few integer variables (`closest_sum`, `cur_sum`, `lo`, `hi`), requiring constant extra memory (ignoring the internal memory used by the sorting algorithm).

--- 

### 2. Brute Force Approach (Alternative)

The brute force method checks every possible triplet combination using three nested loops. It calculates the sum for each triplet and updates the closest sum if a better one is found. 

```python
class SolutionBruteForce:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        # Time Complexity: O(N^3)
        # Space Complexity: O(1)
        n = len(nums)
        closest_sum = float('inf')
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if abs(cur_sum - target) < abs(closest_sum - target):
                        closest_sum = cur_sum
                        
        return closest_sum
```

**Time Complexity:** $O(N^3)$
Checking all possible triplets takes cubic time.
**Space Complexity:** $O(1)$
No extra memory structures are used.