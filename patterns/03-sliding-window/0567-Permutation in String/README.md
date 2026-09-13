> 💡 **Note:** This problem is solved using the **Sliding Window** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [567. Permutation in String](https://leetcode.com/problems/permutation-in-string/)

Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.

In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

### Example 1:
> **Input:** `s1 = "ab", s2 = "eidbaooo"`
> **Output:** `true`
> **Explanation:** `s2` contains one permutation of `s1` ("ba").

### Example 2:
> **Input:** `s1 = "ab", s2 = "eidboaoo"`
> **Output:** `false`

---

### 1. Fixed-Size Sliding Window with Hash Maps (Optimal)

* A permutation simply means that the substring has the exact same frequencies of each character as `s1`. Order does not matter.
* We can use a **Fixed-Size Sliding Window** of length `len(s1)` to slide across `s2`.
* First, we record the frequency of characters in `s1` into a dictionary (`letters_1`).
* As our right pointer (`r`) iterates through `s2`, we add the current character to a second dictionary (`letters_2`).
* When our window reaches the required size `(r - l + 1) == len(s1)`, we compare the two dictionaries. If they match, we found a permutation and return `True`.
* Before moving the window forward, we must remove the character at the left pointer (`s2[l]`) from `letters_2`. If its frequency drops to zero, we explicitly delete the key from the dictionary to ensure clean equality checks. Then we increment `l`.

```python
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters_1 = {}
        letters_2 = {}
        
        for l in s1:
            letters_1[l] = letters_1.get(l, 0) + 1
            
        l = 0
        for r in range(len(s2)):
            letters_2[s2[r]] = letters_2.get(s2[r], 0) + 1
            
            if (r - l + 1) == len(s1):
                if letters_1 == letters_2:
                    return True
                    
                letters_2[s2[l]] -= 1
                if letters_2[s2[l]] == 0:
                    del letters_2[s2[l]]
                l += 1
                
        return False
```

**Time Complexity:** `O(N + M)`

Let `N` be the length of `s1` and `M` be the length of `s2`. We iterate through `s1` and `s2` once. Although comparing two dictionaries takes up to `K` operations (where `K` is the number of unique characters), since the alphabet is limited to 26 lowercase English letters, `K` is a constant (`K <= 26`). Therefore, the complexity does not become `O(N + M * K)`; it simplifies cleanly to `O(N + M)`.

**Space Complexity:** `O(1)`

Both `letters_1` and `letters_2` store at most 26 key-value pairs. Since the memory used is bounded by a constant, the space complexity is strictly `O(1)`.

--- 

### 2. Sorting Substrings (Brute Force)

* We can sort `s1` alphabetically.
* Then, we can iterate through every possible substring of length `len(s1)` in `s2`, sort each substring, and compare it to the sorted `s1`.
* If they match, it's a permutation. This approach is highly inefficient due to repeated sorting.

```python
class SolutionBruteForce:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        sorted_s1 = sorted(s1)
        
        for i in range(m - n + 1):
            if sorted(s2[i:i+n]) == sorted_s1:
                return True
                
        return False
```

**Time Complexity:** `O(M * N \log N)`

For every starting index in `s2` (which takes `O(M)` iterations), we extract a substring of length `N` and sort it in `O(N \log N)` time. 

**Space Complexity:** `O(N)`

We create new string/list allocations for `sorted_s1` and the sliced substrings.