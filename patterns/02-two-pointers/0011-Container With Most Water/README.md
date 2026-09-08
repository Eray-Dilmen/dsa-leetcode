> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

**Problem Statement**
You are given an integer array `height` where each element represents the height of a vertical line drawn on a coordinate plane. The distance between each line is 1 on the x-axis. Find two lines that, together with the x-axis, form a container capable of holding the maximum amount of water. Return this maximum area. You cannot slant the container.

### Example 1:
**Input:** `height = [1,8,6,2,5,4,8,3,7]`  
**Output:** `49`  
**Explanation:** The maximum water is trapped between the lines at index 1 (height 8) and index 8 (height 7). The width is 7, and the limiting height is 7. Area = 7 * 7 = 49.

### Example 2:
**Input:** `height = [1,1]`  
**Output:** `1`  

---

### 1. Two Pointers Approach (Optimal)

To maximize the area of water, we need to balance **width** and **height**. The area is always limited by the shorter line (`min(height[left], height[right])`). 
We can start by maximizing the width: placing one pointer at the very beginning and one at the very end of the array. To find a potentially larger area, we must compensate for the shrinking width by finding taller lines. Therefore, we always move the pointer that points to the **shorter** line inward, hoping to encounter a taller line.

```python
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Space Complexity = O(1)
        left = 0
        right = len(height) - 1
        max_area = 0
        
        # Time Complexity = O(N)
        while left < right:
            w = right - left
            h = min(height[left], height[right])
            a = w * h
            max_area = max(max_area, a)
            
            # Move the pointer of the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_area
```

**Time Complexity:** $O(N)$
We traverse the array exactly once, moving the pointers towards each other until they meet.
**Space Complexity:** $O(1)$
We only use a few integer variables to keep track of pointers and the maximum area, requiring constant extra memory.

--- 

### 2. Brute Force Approach (Time Limit Exceeded)

A naive approach is to calculate the area for every possible pair of lines in the array using nested loops, and keep track of the maximum area found.

```python
class SolutionBruteForce:
    def maxArea(self, height: list[int]) -> int:
        # Space Complexity = O(1)
        max_area = 0
        
        # Time Complexity = O(N^2)
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = j - i
                h = min(height[i], height[j])
                max_area = max(max_area, w * h)
                
        return max_area
```

**Time Complexity:** $O(N^2)$
Testing every single pair results in a quadratic time complexity, which is too slow for large inputs and will cause a Time Limit Exceeded (TLE) error.
**Space Complexity:** $O(1)$
No extra memory is dynamically allocated.