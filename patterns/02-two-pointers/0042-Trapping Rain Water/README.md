> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

**Problem Statement**
Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

### Example 1:
<img src="trapping_rain_water.png" width="500" />

> **Input:** `height = [0,1,0,2,1,0,1,3,2,1,2,1]`  
> **Output:** `6`  
> **Explanation:** The above elevation map (black section) is represented by array `[0,1,0,2,1,0,1,3,2,1,2,1]`. In this case, 6 units of rain water (blue section) are being trapped.

### Example 2:
> **Input:** `height = [4,2,0,3,2,5]`  
> **Output:** `9`  

---

### 1. Two Pointers Approach (Optimal)

The amount of water a single block can trap is determined by the minimum of the highest walls to its left and right, minus its own height. Instead of calculating the absolute maximums for every block beforehand, we can use two pointers from both ends. 

By maintaining a `leftMax` and a `rightMax`, we can decide which side securely bounds the water. If `leftMax < rightMax`, we know for a fact that the water level at the `left` pointer is bounded by `leftMax`, regardless of what happens in the middle. We calculate the trapped water for the `left` pointer, move it inward, and repeat. This allows us to calculate the trapped water on the fly, reducing the space complexity to $O(1)$.

```python
class Solution:
    def trap(self, height: list[int]) -> int:
        # Space Complexity = O(1) -> No extra arrays used
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0
        
        # Time Complexity = O(N) -> Single pass through the array
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(0, leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(0, rightMax - height[r])
                
        return res
```

**Time Complexity:** $O(N)$
The two pointers iterate through the array exactly once, meeting in the middle.
**Space Complexity:** $O(1)$
Only a few variables (`l`, `r`, `leftMax`, `rightMax`, `res`) are used, requiring constant extra memory.

--- 

### 2. Dynamic Programming / Prefix Arrays Approach (Alternative)

Instead of evaluating on the fly, we can precompute the maximum wall height to the left and the maximum wall height to the right for every single position in the array. We store these values in two separate arrays (`max_left` and `max_right`). Then, we iterate through the array one last time to calculate the trapped water at each index. 

While easier to conceptualize, storing these precomputed values forces us to use extra memory.

```python
class SolutionAlternative:
    def trap(self, height: list[int]) -> int:
        # Space Complexity = O(N) -> Allocating two arrays of size N
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        
        # Time Complexity = O(N)
        for i in range(n):
            j = -i - 1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])
            
        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])
            
        return summ
```

**Time Complexity:** $O(N)$
We iterate through the array a few times, which simplifies to $O(N)$.
**Space Complexity:** $O(N)$
We allocate two additional arrays of size $N$ (`max_left` and `max_right`).

---

### 3. Brute Force Approach (Time Limit Exceeded)

For every element in the array, we can iterate all the way to its left to find the absolute maximum wall, and then iterate all the way to its right to find the absolute maximum wall. 

```python
class SolutionBruteForce:
    def trap(self, height: list[int]) -> int:
        # Space Complexity = O(1)
        res = 0
        n = len(height)
        
        # Time Complexity = O(N^2)
        for i in range(n):
            left_max = max(height[:i+1]) if i >= 0 else 0
            right_max = max(height[i:]) if i < n else 0
            res += min(left_max, right_max) - height[i]
            
        return res
```

**Time Complexity:** $O(N^2)$
For each of the $N$ elements, we scan the rest of the array to find the maximums. This leads to a quadratic time complexity, resulting in a Time Limit Exceeded (TLE) error.
**Space Complexity:** $O(1)$
No extra memory is utilized beyond basic variables.