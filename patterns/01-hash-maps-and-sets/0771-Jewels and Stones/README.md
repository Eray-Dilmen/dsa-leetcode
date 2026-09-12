> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [771. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/)

**Problem Statement**
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so `"a"` is considered a different type of stone from `"A"`.

### Example 1:
> **Input:** `jewels = "aA"`, `stones = "aAAbbbb"`  
> **Output:** `3`

### Example 2:
> **Input:** `jewels = "z"`, `stones = "ZZ"`  
> **Output:** `0`

> **Note:** The Hash Set pattern is used to store elements in a set to find them later in `O(1)` time, instead of repeatedly scanning the array or string from start to finish (which takes `O(n)` time).

---

### 1. Hash Set Approach (Optimal)

Instead of using a string, we use a Hash Set which allows for `O(1)` time complexity for lookups. The operation is divided into two independent stages:

1. **Stage 1 (Set Creation):** We take all characters in the `jewels` string and insert them into a Set (`s = set(jewels)`). Inserting `n` characters into a hash table takes `O(n)` time.
2. **Stage 2 (Checking Stones):** We set up a single loop over the `stones` string (`m` steps). For each stone, we perform a `stone in s` check. Since searching in a Set is `O(1)`, checking each stone is instantaneous (`m * O(1) = O(m)`).

```python
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = set(jewels)
        count = 0
        
        for stone in stones:
            if stone in s:
                count += 1
                
        return count
```

**Time Complexity:** `O(n + m)`

Creating the set takes `O(n)` time, and iterating through the stones takes `O(m)` time. Since these operations are consecutive rather than nested, we add them together (`n + m`).

**Space Complexity:** `O(n)`

We use a Hash Set to store the characters from the `jewels` string, taking up memory proportional to `n`.

--- 

### 2. Brute Force Approach

For every single stone in `stones` (`m` times), the `jewels` string is scanned entirely (`n` times). The `in` operator in Python runs a hidden `O(n)` for-loop in the background when used on a string.

* For the first stone, `n` checks are made.
* For the second stone, another `n` checks are made.
* **Total operations:** `m` times `n` searches = `m * n` steps.

```python
class SolutionBruteForce:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        
        for stone in stones:
            if stone in jewels:
                count += 1
                
        return count
```

**Time Complexity:** `O(n * m)`

The combination of the explicit `for` loop and the implicit `in` operator string search creates a nested loop scenario.

**Space Complexity:** `O(1)`

No additional data structure is created.