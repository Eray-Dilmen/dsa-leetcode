💡 **Note:** This problem is solved using the **Sliding Window** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [3. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

Given a string `s`, find the length of the longest substring without duplicate characters.

### Example 1:
> **Input:** `s = "abcabcbb"`  
> **Output:** `3`  
> **Explanation:** The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

### Example 2:
> **Input:** `s = "bbbbb"`  
> **Output:** `1`  
> **Explanation:** The answer is "b", with the length of 1.

### Example 3:
> **Input:** `s = "pwwkew"`  
> **Output:** `3`  
> **Explanation:** The answer is "wke", with the length of 3. Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

---

### 1. Sliding Window with Set Approach (Optimal)

* We use two pointers, `l` (left) and `r` (right), to represent a sliding window of unique characters. 
* We expand the window by moving `r` to the right and adding each character to a `Set`. 
* If we encounter a character at `r` that is already in our `Set`, it means we have a duplicate. To fix this, we must shrink our window from the left. 
* We repeatedly remove the character at index `l` from the `Set` and increment `l` until the duplicate character is completely removed from our current window. 
* After ensuring the window only contains unique characters, we add the new character at `r` to the `Set` and update our maximum recorded length.

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        longest = 0
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            
            w = r - l + 1
            longest = max(longest, w)
            sett.add(s[r])
            
        return longest
```

**Time Complexity:** `O(N)`

We traverse the string at most twice (once by the `r` pointer and once by the `l` pointer). This results in a linear time complexity.

**Space Complexity:** `O(min(M, N))`

The `Set` stores the unique characters in the current window. The space is bounded by the size of the string `N` and the size of the character set `M`.

--- 

### 2. Nested Loops Approach (Brute Force)

* We can check every possible substring by using two nested loops. The outer loop picks a starting index, and the inner loop expands the substring character by character. 
* We use a `Set` to keep track of characters in the current substring. 
* If a character repeats, we immediately stop expanding that specific substring and move to the next starting index. This avoids `O(N^3)` time but still results in an inefficient `O(N^2)` complexity.

```python
class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        n = len(s)
        
        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)
                
        return max_len
```

**Time Complexity:** `O(N^2)`

Checking every possible substring starting from each index requires expanding a nested loop, leading to a quadratic time complexity.

**Space Complexity:** `O(min(M, N))`

We use a `Set` to track characters for each substring being evaluated.