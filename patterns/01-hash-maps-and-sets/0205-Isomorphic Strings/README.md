> 💡 **Note:** This problem is optimally solved using the **Hash Map** pattern to establish a 1-to-1 mapping (bijection). For the theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [0205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/)

Given two strings `s` and `t`, determine if they are isomorphic.

Two strings `s` and `t` are isomorphic if the characters in `s` can be replaced to get `t`.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

### Example 1:
> **Input:** `s = "egg", t = "add"`  
> **Output:** `true`  
> **Explanation:** The strings `s` and `t` can be made identical by mapping 'e' to 'a' and 'g' to 'd'.

### Example 2:
> **Input:** `s = "foo", t = "bar"`  
> **Output:** `false`  
> **Explanation:** The strings `s` and `t` can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

### Example 3:
> **Input:** `s = "paper", t = "title"`  
> **Output:** `true`  

---

### 1. Two Hash Maps Approach (Optimal)

To determine if two strings are isomorphic, we need to ensure a strict 1-to-1 mapping (bijection) between their characters. This means:
1. A character in `s` must always map to the exact same character in `t`.
2. A character in `t` must always be mapped from the exact same character in `s`.

We can achieve this by maintaining two separate Hash Maps (`map_st` and `map_ts`). As we iterate through the strings side by side, we cross-check both maps. If a character is already mapped to someone else, we immediately return `False`.

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        map_st = {}
        map_ts = {}
        
        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]
            
            # 1. Check: Who did char_s map to before?
            if char_s in map_st and map_st[char_s] != char_t:
                return False
                
            # 2. Check: Who did char_t map to before?
            if char_t in map_ts and map_ts[char_t] != char_s:
                return False
                
            # If no issues, record the mapping
            map_st[char_s] = char_t
            map_ts[char_t] = char_s
            
        return True
```

**Time Complexity:** `O(N)`  
We iterate through the strings exactly once. Dictionary lookups and insertions take `O(1)` time on average, resulting in an overall linear time complexity.

**Space Complexity:** `O(1)`  
The size of the hash maps depends on the number of unique characters. Since the character set is bounded (e.g., 256 ASCII characters), the space complexity is strictly $O(1)$.

--- 

### 2. First Occurrence Index Approach (Brute Force)

A clever but less efficient alternative is to compare the *first occurrence index* of each character. If two strings are isomorphic, the structure of their repeated characters must perfectly align. 

By using the `find()` method, we can check where a specific character *first* appeared in the string. If the first occurrence index of `s[i]` does not match the first occurrence index of `t[i]`, it means the pattern of repetition is broken.

```python
class SolutionBruteForce:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # If lengths are different, they cannot be mapped
        if len(s) != len(t):
            return False
            
        for i in range(len(s)):
            # Does the first occurrence index of s[i] in s
            # match the first occurrence index of t[i] in t?
            if s.find(s[i]) != t.find(t[i]):
                return False
                
        return True
```

**Time Complexity:** `O(N^2)`  
The `for` loop runs $N$ times, and inside the loop, the `find()` function takes $O(N)$ time to scan the string from the beginning for each character. This results in a quadratic time complexity, which is highly inefficient for large strings.

**Space Complexity:** `O(1)`  
We do not use any additional data structures, keeping the extra space constant.