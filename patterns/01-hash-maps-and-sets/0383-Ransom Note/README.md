> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [383. Ransom Note](https://leetcode.com/problems/ransom-note/)

**Problem Statement**
Given two strings `ransomNote` and `magazine`, return `true` if `ransomNote` can be constructed by using the letters from `magazine` and `false` otherwise.
Each letter in `magazine` can only be used once in `ransomNote`.

### Example 1:
> **Input:** `ransomNote = "a"`, `magazine = "b"`  
> **Output:** `false`

### Example 2:
> **Input:** `ransomNote = "aa"`, `magazine = "ab"`  
> **Output:** `false`

### Example 3:
> **Input:** `ransomNote = "aa"`, `magazine = "aab"`  
> **Output:** `true`

> **Note:** The Hash Map pattern is used to count the frequencies of elements in a string or array, allowing for `O(1)` time lookups and verifications later.

---

### 1. Hash Map Approach (Optimal)

* First, we iterate through all the characters in `magazine` and record their frequencies in a dictionary (Hash Map).
* Next, we iterate through the characters of `ransomNote` and check if the character exists in the dictionary and if its count is greater than zero (`> 0`).
* If it exists and is available, we decrement its count by 1 and continue. If it doesn't exist or the count is zero, we immediately return `False`.

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        guide = {}

        for letter in magazine:
            if letter in guide:
                guide[letter] += 1
            else:
                guide[letter] = 1

        for char in ransomNote:
            if char not in guide or guide[char] == 0:
                return False
            guide[char] -= 1

        return True
```

**Time Complexity:** `O(m + n)`

The first loop runs for the length of `magazine` (`m`), taking `O(m)` time. The second loop runs for the length of `ransomNote` (`n`), taking `O(n)` time. Since these loops are consecutive and not nested, their complexities are added. Dictionary lookups (`in`) take `O(1)` time. Thus, the total time complexity is `O(m + n)`.

**Space Complexity:** `O(1)`

We created an extra dictionary named `guide`. Even in the worst-case scenario, the English alphabet only contains 26 lowercase letters. This means the dictionary size is capped at 26 elements, regardless of the input size. Since the memory footprint is bounded by a constant, the space complexity is `O(1)`.

--- 

### 2. Brute Force Approach

```python
class SolutionBruteForce:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_list = list(magazine)
        
        for char in ransomNote:
            if char in mag_list:
                mag_list.remove(char)
            else:
                return False
                
        return True
```

**Time Complexity:** `O(n * m)`

For each character (`n`) in `ransomNote`, we perform both a lookup (`in`) and a deletion (`remove`) operation on the `mag_list`. Because these list operations take `O(m)` time, the total time complexity becomes `O(n * m)`.

**Space Complexity:** `O(m)`

Since strings are immutable in Python, we create an additional list (`mag_list`) to hold the characters of `magazine` so we can perform deletion operations. This list requires space proportional to `m`.