> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [15. 3Sum](https://leetcode.com/problems/3sum/)


Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

### Example 1:
> **Input:** `nums = [-1,0,1,2,-1,-4]`  
> **Output:** `[[-1,-1,2],[-1,0,1]]`  
> **Explanation:**  
> nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.  
> nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.  
> nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.  
> The distinct triplets are [-1,0,1] and [-1,-1,2].  
> Notice that the order of the output and the order of the triplets does not matter.

### Example 2:
> **Input:** `nums = [0,1,1]`  
> **Output:** `[]`  
> **Explanation:** The only possible triplet does not sum up to 0.  

### Example 3:
> **Input:** `nums = [0,0,0]`  
> **Output:** `[[0,0,0]]`  
> **Explanation:** The only possible triplet sums up to 0.

---

### 1. Two Pointers & Hash Set Approach (Optimal)

To find three numbers that sum to zero, we can fix one number (`nums[i]`) and use the **Two Pointers** technique to find the other two numbers. 
First, we sort the array. Sorting allows us to effectively move our `left` and `right` pointers based on whether the current sum is too large or too small. 

To ensure we do not return duplicate triplets, we store our valid triplets in a **Hash Set** (`set()`) as tuples.

> ⚠️ **Common Mistake: Checking uniqueness using a List (`not in`)**
> 
> ```python
> # ❌ INEFFICIENT WAY
> l = []
> if nums[i] + nums[left] + nums[right] == 0 and [nums[i], nums[left], nums[right]] not in l:
>     l.append([nums[i], nums[left], nums[right]])
> ```
> Searching inside a list using `not in l` takes `O(k)` time, where `k` is the current size of the list. Because this search happens inside a nested loop, your total time complexity drastically degrades, eventually causing a **Time Limit Exceeded (TLE)** error. 
> 
> **The Solution:** By defining `l = set()` and adding elements as tuples (`l.add((...))`), duplicate handling is done automatically. Searching/inserting in a Set takes `O(1)` time, making the algorithm extremely fast and efficient.

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Space Complexity = O(n) -> Storing unique triplets in a set
        nums.sort()
        l = set()
        
        # Time Complexity = O(n^2)
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    l.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif total > 0:
                    k -= 1
                else:
                    j += 1
                    
        return list(l)
```

**Time Complexity:** `O(n^2)` Sorting the array takes `O(n log n)`. The `for` loop runs `n` times, and the `while` loop (Two Pointers) takes `O(n)` time for each iteration. `O(n log n) + O(n^2)` simplifies asymptotically to `O(n^2)`.

**Space Complexity:** `O(n)` The space complexity is bounded by the Hash Set used to store the unique valid triplets, which can grow linearly with the input size in the worst case. Sorting may also take `O(n)` or `O(log n)` depending on the language's sorting algorithm.

--- 

### 2. Brute Force Approach

We set up three nested loops to check every possible combination of three numbers in the array. If they add up to `0`, we add them to a set to avoid duplicates.

```python
class SolutionBruteForce:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # Space Complexity = O(n)
        # Time Complexity = O(n^3)
        nums.sort()
        l = set()
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        l.add((nums[i], nums[j], nums[k]))
                        
        return list(l)
```

**Time Complexity:** `O(n^3)` Three nested loops traverse the array, leading to a cubic time complexity. This will trigger a TLE (Time Limit Exceeded) for large arrays.

**Space Complexity:** `O(n)` We still need extra space for the set to manage the unique valid triplets.