> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

Given an integer array `nums` sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

### Example 1:
> **Input:** `nums = [-4,-1,0,3,10]`  
> **Output:** `[0,1,9,16,100]`  
> **Explanation:** After squaring, the array becomes `[16,1,0,9,100]`. After sorting, it becomes `[0,1,9,16,100]`.

### Example 2:
> **Input:** `nums = [-7,-3,2,3,11]`  
> **Output:** `[4,9,9,49,121]`  

---

### 1. Two Pointers & Reverse Approach (Optimal)

* Because the input array is already sorted but contains negative numbers, squaring the numbers creates a "V" shape in terms of values: the largest squares will always be at the extreme edges (either the large negative numbers at the beginning or the large positive numbers at the end), and the smallest squares will be near zero in the middle. 
* We can use the **Two Pointers** pattern to compare the extreme ends, pick the largest square, and build our result array.

**Algorithmic Details & "Why"s:**
* **Why check for Max (`>`) instead of Min (`<`)?:** Since we know the absolute largest values are at the edges, it is much easier to compare the two ends and extract the maximums one by one. If we tried to find the minimums first, we would have to somehow find the "zero point" (the center of the V-shape) and expand outwards, which is overly complicated.
* **Why `while left <= right:` instead of `<`?:** If we used `<`, the loop would terminate when both pointers point to the exact same middle element. That last remaining element would be skipped and not added to our result. Using `<=` ensures every single element is processed.
* **Why use `.reverse()`?:** Because we extract the *largest* elements first and append them to our `result` array, our list ends up in descending order (largest to smallest). To satisfy the problem's ascending order requirement, we reverse the list at the very end. The `.reverse()` operation takes `O(N)` time. Since `O(N)` (Two Pointers) + `O(N)` (Reverse) = `O(N)`, it does not negatively impact our overall linear time complexity.
* **Why use an extra `result[]` array? (Space Complexity):** Could we do this in-place to save memory? No, not without ruining the time complexity. If we tried to insert elements at the beginning of the existing array, we would have to shift all other elements to the right, which takes `O(N)` time per insertion (making the algorithm `O(N^2)`). To maintain an `O(N)` time complexity, allocating an extra array (`O(N)` space) is absolutely mandatory.

```python
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = []
        
        while left <= right:
            if nums[left]**2 > nums[right]**2:
                result.append(nums[left]**2)
                left += 1
            else:
                result.append(nums[right]**2)
                right -= 1
                
        result.reverse()
        return result
```

**Time Complexity:** `O(N)`

We traverse the array once using pointers (`O(N)`), and reversing the result takes another `O(N)`. Total time is `O(N)`.

**Space Complexity:** `O(N)`

We allocate a new `result` array of size N to hold our squared values.

--- 

### 2. Squaring and Sorting Approach (Alternative / Brute Force)

* A very straightforward way to solve this is to simply iterate through the array, square every element in place, and then call the built-in sort function. 
* While this code is extremely short and easy to read, the sorting operation makes it slower.

```python
class SolutionSorting:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
            
        nums.sort()
        return nums
```

**Time Complexity:** `O(N log N)`

The built-in sorting algorithm (`Timsort` in Python) dominates the time complexity.

**Space Complexity:** `O(1)` or `O(N)`

Python's `sort()` modifies the list in place but requires `O(N)` extra space internally in the worst case.