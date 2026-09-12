> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [128. Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/)


Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in `O(n)` time.

### Example 1:
> **Input:** `nums = [100,4,200,1,3,2]`  
  **Output:** `4`  
  **Explanation:** The longest consecutive elements sequence is `[1, 2, 3, 4]`. Therefore its length is 4.

### Example 2:
> **Input:** `nums = [0,3,7,2,5,8,4,6,0,1]`  
  **Output:** `9`  

---

### 1. Hash Set Approach (Optimal)

To achieve the strictly required $O(N)$ time complexity, we cannot sort the array (which takes $O(N \log N)$). Instead, we convert the array into a Hash Set. This gives us $O(1)$ lookups.

The brilliant trick here is identifying the **start of a sequence**. A number can only be the beginning of a sequence if its preceding number (`num - 1`) does NOT exist in the set. 
If we find a starting number, we keep checking if `num + 1`, `num + 2`, etc., exist in the set, counting the length of the sequence. By only starting our `while` loop when we are at the true beginning of a sequence, we avoid redundant calculations.

```python
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Space Complexity = O(N) -> Storing unique elements in a set
        s = set(nums)
        longest = 0
        
        # Time Complexity = O(N) -> Each number is visited at most twice
        for num in s:
            # Check if it is the start of a sequence
            if num - 1 not in s:
                next_num = num + 1
                length = 1
                
                # Count the consecutive streak
                while next_num in s:
                    length += 1
                    next_num += 1
                    
                longest = max(longest, length)
                
        return longest
```

**Time Complexity:** $O(N)$
Even though there is a `while` loop inside a `for` loop, the `while` loop only runs when a number is the start of a sequence. This guarantees that the inner loop processes each number in a sequence exactly once. Thus, the total time is strictly linear, $O(N)$.

**Space Complexity:** $O(N)$
Allocating memory for the Hash Set takes linear space based on the number of elements.

--- 

### 2. Sorting Approach (Alternative / Slower)

We can sort the array first and then iterate through it to count consecutive numbers. While logical, sorting forces the time complexity to $O(N \log N)$, which violates the problem's strict $O(N)$ constraint. It is a good fallback to explain during interviews before optimizing.

```python
class SolutionSorting:
    def longestConsecutive(self, nums: list[int]) -> int:
        # Space Complexity = O(1) or O(N) depending on the sorting algorithm
        if not nums:
            return 0
            
        # Time Complexity = O(N log N) -> Sorting the array
        nums.sort()
        
        longest = 1
        current_streak = 1
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    current_streak += 1
                else:
                    longest = max(longest, current_streak)
                    current_streak = 1
                    
        return max(longest, current_streak)
```

**Time Complexity:** $O(N \log N)$
The dominant operation is the built-in `.sort()` method.

**Space Complexity:** $O(1)$ or $O(N)$
Depending on the language's sorting algorithm (Timsort in Python takes $O(N)$ space).