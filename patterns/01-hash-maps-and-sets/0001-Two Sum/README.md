> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [1. Two Sum](https://leetcode.com/problems/two-sum/)


You are given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

### Example 1:
> **Input:** `nums = [2,7,11,15]`, `target = 9`  
> **Output:** `[0,1]`  
> **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
> **Input:** `nums = [3,2,4]`, `target = 6`  
> **Output:** `[1,2]`

### Example 3:
> **Input:** `nums = [3,3]`, `target = 6`  
> **Output:** `[0,1]`

> **Note:** The Hash Table pattern is used to store elements and their indices in a dictionary (Hash Map) to find them later in `O(1)` time, instead of repeatedly scanning the array from start to finish (which takes `O(n)` time).

---

### 1. Hash Map Approach (Optimal)

* We iterate through the array once. At each step, we find the required "complement" by subtracting the current number from the target (`target - num`).
* If this complement exists in our Hash Map, we have found our match; we return the indices of both numbers.
* If it does not exist, we save the current number and its index into the Hash Map (`mapping[num] = index`) and proceed to the next number.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mapping = {} # Space Complexity = O(n)

        # Time Complexity = O(n)
        for index, num in enumerate(nums):
            if (target - num) in mapping:
                return [mapping[target - num], index]
            else:
                mapping[num] = index
```

**Time Complexity:** `O(n)`

The entire array is traversed only once using a single `for` loop, which takes `O(n)` time. Checking if an element exists in a Python dictionary takes `O(1)` time on average.

**Space Complexity:** `O(n)`

We created an extra dictionary (`mapping`) to store the numbers and their indices. In the worst-case scenario, we might need to insert all elements into this dictionary, making the space scale linearly with the input size.

--- 

### 2. Brute Force Approach

* We set up nested loops to try every possible pair.
* The outer loop picks the first number, and the inner loop checks every subsequent number to see if their sum equals the `target`.
* This method is inefficient because it repeatedly scans the rest of the array for every single element.

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Space Complexity = O(1)
        # Time Complexity = O(n^2)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

**Time Complexity:** `O(n^2)`

For every element in the array (`n`), the rest of the elements are checked. The nested loop structure brings the complexity to `O(n^2)`.

**Space Complexity:** `O(1)`

No additional data structures (like arrays or hash maps) are used, so the memory footprint remains constant.