> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.
The tests are generated such that there is exactly one solution. You may not use the same element twice.
Your solution must use only constant extra space.

### Example 1:
> **Input:** `numbers = [2,7,11,15]`, `target = 9`  
> **Output:** `[1,2]`  
> **Explanation:** The sum of 2 and 7 is 9. Therefore, `index1 = 1`, `index2 = 2`. We return `[1, 2]`.

### Example 2:
> **Input:** `numbers = [2,3,4]`, `target = 6`  
> **Output:** `[1,3]`  
> **Explanation:** The sum of 2 and 4 is 6. Therefore `index1 = 1`, `index2 = 3`. We return `[1, 3]`.

---

### 1. Two Pointers Approach (Optimal)

* Because the array is already sorted, we can use the **Two Pointers** pattern to find the target sum in `O(n)` time without needing extra memory like a Hash Map.
* We place one pointer at the beginning (`left`) and one at the end (`right`). We calculate the sum of the elements at these two pointers.
* If the sum matches the `target`, we found our answer (adding 1 to the indices because it is 1-indexed).
* If the sum is **greater** than the target, the current sum is too large. We can decrease it by moving the `right` pointer one step to the left (pointing to a smaller number).
* If the sum is **less** than the target, the current sum is too small. We can increase it by moving the `left` pointer one step to the right (pointing to a larger number).

```python
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] == target:
                return [left + 1, right + 1]
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                left += 1
```

**Time Complexity:** `O(N)`

In the worst-case scenario, the `left` and `right` pointers will meet in the middle, meaning we traverse the array at most once.

**Space Complexity:** `O(1)`

We only use two integer variables (`left` and `right`) to store indices, fulfilling the strict constant extra space requirement of the problem.

--- 

### 2. Brute Force Approach (Time Limit Exceeded)

* We set up nested loops to check every possible pair of numbers to see if their sum equals the `target`. 
* While this logic is correct, it completely ignores the fact that the array is already sorted. 
* As seen in the analysis, this approach is highly inefficient for large arrays and results in a **Time Limit Exceeded (TLE)** error.

```python
class SolutionBruteForce:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
```

**Time Complexity:** `O(N^2)`

For every element in the array, we scan the rest of the array. The nested loop structure brings the time complexity to `O(N^2)`.

**Space Complexity:** `O(1)`

No additional data structures are used.