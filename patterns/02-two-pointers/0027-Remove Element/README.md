> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [27. Remove Element](https://leetcode.com/problems/remove-element/)

Suppose you have an integer array `nums` and a specific integer `val`. Your objective is to eliminate all instances of `val` from the array `nums` modifying it strictly in-place (without allocating another array). The order of the kept elements can be changed. You must return `k`, which represents the count of elements that are not equal to `val`. The judging system will verify that the first `k` positions of your array contain these valid elements.

### Example 1:
> **Input:** `nums = [3,2,2,3], val = 3`  
> **Output:** `2, nums = [2,2,_,_]`  

### Example 2:
> **Input:** `nums = [0,1,2,2,3,0,4,2], val = 2`  
> **Output:** `5, nums = [0,1,4,0,3,_,_,_]`  

---

### 1. In-Place Two Pointers Approach (Optimal)

This is the optimal solution provided in your screenshot. We utilize a fast and slow pointer concept. 

The `for` loop acts as our fast pointer (`i`), iterating through every single element in the array to check if it equals `val`. The variable `k` acts as our slow pointer, keeping track of the index where the next valid (non-`val`) element should be placed. Whenever we find a valid element, we overwrite the value at index `k` with this valid element and increment `k`. This naturally pushes all `val` elements out of the first `k` positions.

```python
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

**Time Complexity:** `O(N)`

We traverse the array exactly once with the `for` loop, making it a linear time operation.

**Space Complexity:** `O(1)`

We only use an integer variable `k` for tracking the index, and we modify the array strictly in-place, so no extra memory is allocated.

--- 

### 2. Built-in Remove Approach (Alternative / Brute Force)

We can repeatedly use Python's built-in `in` operator and `remove()` method to find and delete the target value. While this satisfies the in-place requirement, it is highly inefficient because both searching for the value and removing it (which requires shifting all subsequent elements to the left) take linear time.

```python
class SolutionBruteForce:
    def removeElement(self, nums: list[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
```

**Time Complexity:** `O(N^2)`

The `in` operator takes `O(N)` time to search, and the `remove()` method also takes `O(N)` time to shift elements left. Doing this repeatedly inside a `while` loop leads to a quadratic time complexity.

**Space Complexity:** `O(1)`

Despite being slow, this method still modifies the list in-place without needing extra data structures.