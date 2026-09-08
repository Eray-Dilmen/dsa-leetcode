> 💡 **Note:** This problem is solved using the **Two Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [125. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)

**Problem Statement**
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

### Example 1:
**Input:** `s = "A man, a plan, a canal: Panama"`  
**Output:** `true`  
**Explanation:** "amanaplanacanalpanama" is a palindrome.  

### Example 2:
**Input:** `s = "race a car"`  
**Output:** `false`  
**Explanation:** "raceacar" is not a palindrome.  

---

### 1. In-Place Two Pointers Approach (Optimal)

To achieve the best performance, we can use the **Two Pointers** technique directly on the original string without creating any new filtered strings or arrays. 

**Algorithmic Logic & The Power of `continue`:**
* We start with `left` at the beginning and `right` at the end of the string.
* We only care about alphanumeric characters (letters and numbers). If `s[left]` is a space or punctuation (`not s[left].isalnum()`), we just move the pointer (`left += 1`) and use the **`continue`** statement. 
* **What `continue` does:** It instantly skips the rest of the current loop iteration and jumps back to the top of the `while` loop. This forces the loop to re-evaluate the new `left` pointer until it finally lands on a valid character. The same logic applies to the `right` pointer.
* **Why this is optimal:** By skipping invalid characters on the fly, we compare the valid letters directly. We don't need to store a "cleaned" version of the string in memory. This brings our space complexity down to a perfect **$O(1)$**, compared to the $O(N)$ space required by the alternative approach.

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Space Complexity = O(1) -> No extra arrays or strings are created
        left = 0
        right = len(s) - 1
        
        # Time Complexity = O(N) -> We traverse the string exactly once
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
                
            if not s[right].isalnum():
                right -= 1
                continue
                
            if s[left].lower() != s[right].lower():
                return False
                
            left += 1
            right -= 1
            
        return True
```

**Time Complexity:** $O(N)$
We process each character in the string at most once.
**Space Complexity:** $O(1)$
We only use two integer pointers, requiring constant extra memory.

--- 

### 2. Array Filtering & Two Pointers (Alternative)

Instead of skipping characters on the fly, we first loop through the string and append only valid, lowercase characters to a new array called `nonalpha`. Then, we apply the standard Two Pointers logic on this clean array. While easier to conceptualize, storing the valid characters forces us to allocate $O(N)$ extra memory.

```python
class SolutionAlternative:
    def isPalindrome(self, s: str) -> bool:
        # Space Complexity = O(N) -> We allocate memory for the 'nonalpha' array
        nonalpha = []
        
        # Time Complexity = O(N) -> O(N) to filter + O(N) to check palindrome
        for i in range(len(s)):
            if s[i].isalnum():
                nonalpha.append(s[i].lower())
                
        left = 0
        right = len(nonalpha) - 1
        
        while left < right:
            if nonalpha[left] != nonalpha[right]:
                return False
            left += 1
            right -= 1
            
        return True
```

**Time Complexity:** $O(N)$
Filtering the string takes $O(N)$, and checking the palindrome takes $O(N)$. Total time is $O(N)$.
**Space Complexity:** $O(N)$
The `nonalpha` array can grow up to the size of the original string.

---

### 3. Built-in Reverse Approach (Brute Force)

We can filter the string into a new cleaned list, and simply compare it to a reversed copy of itself using Python's slicing `[::-1]`.

```python
class SolutionBruteForce:
    def isPalindrome(self, s: str) -> bool:
        # Space Complexity = O(N) -> For 'cleaned' array and its reversed copy
        # Time Complexity = O(N) -> List comprehension and reversing
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]
```

**Time Complexity:** $O(N)$
**Space Complexity:** $O(N)$