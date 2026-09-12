> 💡 **Note:** This problem is solved using the **Sliding Window** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

### Example 1:
> **Input:** `s = "ABAB", k = 2`
> **Output:** `4`
> **Explanation:** Replace the two 'A's with two 'B's or vice versa.

### Example 2:
> **Input:** `s = "AABABBA", k = 1`
> **Output:** `4`
> **Explanation:** Replace the one 'A' in the middle with 'B' and form "AABBBBA".
> The substring "BBBB" has the longest repeating letters, which is 4.
> There may exists other ways to achieve this answer too.

---

### 1. Sliding Window with Frequency Map Approach (Optimal)

* We use a sliding window defined by two pointers, `l` (left) and `r` (right), and a hash map (`count`) to keep track of the frequencies of characters within the current window. 
* We also maintain a `max_freq` variable to store the count of the most frequent character in our window.
* As we expand the window by moving `r` to the right, we calculate the number of characters that need to be replaced. 
* The formula for characters to replace is the current window size `(r - l + 1)` minus the frequency of the most common character `max_freq`. 
* If this difference is strictly greater than `k`, our window is invalid, and we must shrink it from the left by incrementing `l` and decrementing the frequency of the character at `s[l]`. We continuously update the `longest` valid window length.

```python
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = {}
        max_freq = 0
        
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1
                
            longest = max(longest, (r - l + 1))
            
        return longest
```

**Time Complexity:** `O(N)`

The right pointer `r` iterates through the string exactly once. The left pointer `l` only moves forward, meaning each character is processed at most twice.

**Space Complexity:** `O(1)`

The hash map stores at most 26 uppercase English letters. Since the size is strictly bounded by 26, the space complexity is constant `O(26) = O(1)`.

--- 

### 2. Nested Loops Approach (Brute Force)

* We check every possible substring starting from each index. 
* For each substring, we use a hash map to count character frequencies and track the maximum frequency. 
* If the length of the current substring minus the maximum frequency is less than or equal to `k`, it's a valid substring, and we update our maximum length. 
* If it exceeds `k`, we can stop expanding this specific substring.

```python
class SolutionBruteForce:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        n = len(s)
        
        for i in range(n):
            count = {}
            max_freq = 0
            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])
                
                if (j - i + 1) - max_freq <= k:
                    longest = max(longest, j - i + 1)
                else:
                    break
                    
        return longest
```

**Time Complexity:** `O(N^2)`

Checking every possible substring involves a nested loop structure, resulting in a quadratic time complexity.

**Space Complexity:** `O(1)`

The hash map is still limited to 26 uppercase English letters, requiring constant memory.