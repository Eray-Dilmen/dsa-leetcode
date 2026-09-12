> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [18. 4Sum](https://leetcode.com/problems/4sum/)

Given an array `nums` of `n` integers, return an array of all the unique quadruplets `[nums[a], nums[b], nums[c], nums[d]]` such that:
* `0 <= a, b, c, d < n`
* `a`, `b`, `c`, and `d` are distinct.
* `nums[a] + nums[b] + nums[c] + nums[d] == target`

You may return the answer in any order.

### Example 1:
> **Input:** `nums = [1,0,-1,0,-2,2], target = 0`  
> **Output:** `[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]`  

### Example 2:
> **Input:** `nums = [2,2,2,2,2], target = 8`  
> **Output:** `[[2,2,2,2]]`  

---

### 1. Sorting & Two Pointers Approach (Optimal)

This is the optimal solution for the 4Sum problem. It builds on the logic of 3Sum. 
By sorting the array first, we can fix the first two numbers using two nested loops (`i` and `j`), and then use the **Two Pointers** technique (`lo` and `hi`) to find the remaining two numbers.
Sorting is crucial because it allows us to easily skip duplicate values, ensuring that our final result only contains unique quadruplets without needing an extra Hash Set.

```python
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        answer = []
        
        nums.sort()
        
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                    
                lo, hi = j + 1, n - 1
                while lo < hi:
                    summ = nums[i] + nums[j] + nums[lo] + nums[hi]
                    
                    if summ == target:
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1
                        
                        # Skip duplicates for the third and fourth numbers
                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
                            
                    elif summ < target:
                        lo += 1
                    else:
                        hi -= 1
                        
        return answer
```

**Time Complexity:** `O(N^3)`

Sorting takes `O(N log N)`. The two outer loops take `O(N^2)` time, and the inner Two Pointers loop takes `O(N)` time. This yields an overall time complexity of `O(N^3)`, which is optimal for 4Sum.

**Space Complexity:** `O(1)` or `O(N)`

We only use variables for tracking indices. However, some sorting algorithms (like Timsort in Python) take `O(N)` space under the hood. The space for the `answer` array is not strictly counted towards auxiliary complexity.

--- 

### 2. Brute Force Approach (Time Limit Exceeded)

The simplest approach is to use four nested loops to check every possible combination of four numbers. 
To handle the "unique quadruplets" constraint, we can sort each valid combination and add it to a Hash Set. 

```python
class SolutionBruteForce:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        unique_quads = set()
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            # Sorting 4 elements is O(1), adding to set is O(1)
                            quad = tuple(sorted((nums[i], nums[j], nums[k], nums[l])))
                            unique_quads.add(quad)
                            
        return [list(q) for q in unique_quads]
```

**Time Complexity:** `O(N^4)`

Checking every combination of 4 elements takes `O(N^4)`. For N=200 (as per constraints), this will definitely result in a Time Limit Exceeded (TLE) error.

**Space Complexity:** `O(N)`

The Hash Set requires memory proportional to the number of unique valid quadruplets found.