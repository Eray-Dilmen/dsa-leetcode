> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [344. Reverse String](https://leetcode.com/problems/reverse-string/)

**Problem Statement**
Write a function that reverses a string. The input string is given as an array of characters `s`.
You must do this by modifying the input array in-place with `O(1)` extra memory.

### Example 1:
> **Input:** `s = ["h","e","l","l","o"]`  
  **Output:** `["o","l","l","e","h"]`

### Example 2:
> **Input:** `s = ["H","a","n","n","a","h"]`  
  **Output:** `["h","a","n","n","a","H"]`

---

### 1. Two Pointers Approach (Optimal)

To reverse an array in-place with strictly $O(1)$ extra memory, we cannot create a new list. Instead, we use the **Two Pointers** technique by placing one pointer at the beginning (`left`) and one at the end (`right`) of the array. 

We swap the elements at these two pointers and then move them towards the center (`left += 1` and `right -= 1`). The loop terminates when the pointers meet in the middle (`left < right`). Python makes this swap extremely clean by allowing tuple unpacking (`a, b = b, a`), completely eliminating the need for a temporary `temp` variable.

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        # Space Complexity = O(1) -> Modifies the array entirely in-place
        left = 0
        right = len(s) - 1
        
        # Time Complexity = O(N) -> Traverses exactly half of the array (N/2 swaps)
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
            
        return s
```

**Time Complexity:** $O(N)$
We only traverse half of the array ($N/2$ swaps), which asymptotically simplifies to $O(N)$ linear time.
**Space Complexity:** $O(1)$
No extra arrays or data structures are created. The array is modified strictly in-place.

--- 

### 2. Built-in Method Approach (Alternative)

Python lists have a built-in `.reverse()` method that reverses the elements in-place. While highly optimized in C under the hood, relying on it bypasses the algorithmic intent of the problem (which is to demonstrate pointer manipulation). It is, however, the most "Pythonic" and practical way to reverse a list in a real-world scenario.

```python
class SolutionAlternative:
    def reverseString(self, s: list[str]) -> None:
        # Space Complexity = O(1) -> Python's internal reverse operates in-place
        # Time Complexity = O(N) -> Reverses N elements
        s.reverse()
        return s
```

**Time Complexity:** $O(N)$
The built-in function touches every element to reverse the array.
**Space Complexity:** $O(1)$
The `.reverse()` method operates in-place without allocating new memory.