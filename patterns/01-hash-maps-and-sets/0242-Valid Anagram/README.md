> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [242. Valid Anagram](https://leetcode.com/problems/valid-anagram/)


Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:
> **Input:** `s = "anagram"`, `t = "nagaram"`  
> **Output:** `true`  

### Example 2:
> **Input:** `s = "rat"`, `t = "car"`  
> **Output:** `false`  

---

### 1. Single Hash Map Approach (Optimal)

If the lengths of the strings are different, they cannot be anagrams. We use a single dictionary to count the frequencies of characters in string `s`. Then, we iterate through string `t`. If a character from `t` is not in our dictionary or its count has reached `0`, we immediately return `False`. Otherwise, we decrement the count. This early exit strategy makes it the most optimal hash map approach.

> 💡 **Code Cleanliness Tip: `count.get(char, 0) + 1`**
> 
> Instead of writing a bulky 4-line `if/else` block to check if a key exists before incrementing it, we use the `.get()` method to achieve the exact same logic in a single, clean line:
> * **How it works:** Normally, accessing a missing key (`count[char]`) throws a `KeyError`. The `.get(key, default)` method safely returns a default value instead.
> * **Parameters:** The first parameter (`char`) is the key we are looking for. The second parameter (`0`) is the default value returned if the key does not exist yet.
> * **Why `+ 1`?:** If the character is new, `.get()` returns `0`, and adding `1` saves it into the dictionary with a value of `1`. If it already exists, `.get()` returns the current count (e.g., `2`), and adding `1` updates it to `3`.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count = {}
        
        # Count characters in s
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        # Decrement using characters in t
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            
        return True
```

**Time Complexity:** `O(n)` Iterating through `s` takes `O(n)` time, and iterating through `t` takes `O(n)` time. Total time is `O(n)`.

**Space Complexity:** `O(1)`
The hash map stores at most 26 lowercase English letters. Since the size is bounded by a constant, the space complexity is `O(1)`.

--- 

### 2. Two Hash Maps Approach (Alternative)

Instead of incrementing and decrementing a single map, we build two separate hash maps to store character frequencies for both `s` and `t`. Finally, we compare the two dictionaries directly. Python handles dictionary equality checks efficiently.

```python
class SolutionTwoMaps:
    def isAnagram(self, s: str, t: str) -> bool:
        sm = {}
        st = {}
        
        for l in s:
            if l in sm:
                sm[l] += 1
            else:
                sm[l] = 1
                
        for l in t:
            if l in st:
                st[l] += 1
            else:
                st[l] = 1
                
        return sm == st
```

**Time Complexity:** `O(n)` Populating both dictionaries takes `O(n)` time.

**Space Complexity:** `O(1)`
Both dictionaries store at most 26 characters, resulting in constant space.

---

### 3. Built-in Counter Approach (Alternative)

Python's `collections` module provides a `Counter` class that automatically builds a frequency map. This is highly pythonic and clean, doing the exact same thing as the Two Hash Maps approach under the hood.

```python
from collections import Counter

class SolutionCounter:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        s_dict = Counter(s)
        t_dict = Counter(t)
        
        return s_dict == t_dict
```

**Time Complexity:** `O(n)`
The `Counter` function iterates through the strings in `O(n)` time.

**Space Complexity:** `O(1)`
The counters store at most 26 characters.

---

### 4. Sorting Approach (Brute Force)

If two strings are anagrams, sorting them alphabetically will result in the exact same string. This approach is very easy to write but inefficient in terms of time complexity due to the sorting algorithm.

```python
class SolutionBruteForce:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
```

**Time Complexity:** `O(n log n)` The sorting operation dominates the time complexity.

**Space Complexity:** `O(n)`
Python's `sorted()` creates new list copies of the strings, using extra linear memory.