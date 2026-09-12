> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [1189. Maximum Number of Balloons](https://leetcode.com/problems/maximum-number-of-balloons/)


Given a string `text`, you want to use the characters of `text` to form as many instances of the word **"balloon"** as possible.
You can use each character in `text` at most once. Return the maximum number of instances that can be formed.

### Example 1:
> **Input:** `text = "nlaebolko"`  
> **Output:** `1`

### Example 2:
> **Input:** `text = "loonbalxballpoon"`  
> **Output:** `2`

### Example 3:
> **Input:** `text = "leetcode"`  
> **Output:** `0`

> **Note:** The Hash Map pattern is used here to count the frequencies of characters in a string, allowing us to perform `O(1)` lookups to determine how many times a specific target word can be formed.

---

### 1. Hash Map Approach (Optimal)

To construct the word "balloon", we need specific amounts of characters: one 'b', one 'a', two 'l's, two 'o's, and one 'n'. We can count the frequencies of all characters in the given `text` using a Dictionary (Hash Map).

The maximum number of words we can form is determined by the character we have the **least** of (the bottleneck). Since 'l' and 'o' appear twice in "balloon", we divide their total counts by 2 to find their true potential. Finally, we take the minimum across all these required character counts.

**Key Details:**
* **Why `.get()`?** If we try to access a key that doesn't exist (e.g., `letters['b']`), Python throws a `KeyError`. Using `letters.get('b', 0)` safely returns `0` if the letter is missing.
* **Why `min()`?** Forming a word is like following a recipe. Even if you have 100 'b's and 'a's, if you only have 1 'n', you can only form 1 "balloon". The `min()` function finds this bottleneck.
* **Why `// 2`?** There are two 'l's and two 'o's in the target word. If you have 5 'l's, integer division `5 // 2` correctly yields 2, which is the maximum number of words those 'l's can support.

```python
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = {}
        
        for letter in text:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
                
        return min(
            letters.get('b', 0),
            letters.get('a', 0),
            letters.get('l', 0) // 2, 
            letters.get('o', 0) // 2, 
            letters.get('n', 0)
        )
```

**Time Complexity:** `O(n)`

We iterate through the string `text` of length `n` exactly once, which takes `O(n)` time. Dictionary reads, writes, and the `min()` operation all take `O(1)` time.

**Space Complexity:** `O(1)`

The Hash Map only stores English lowercase letters (maximum 26 characters). No matter how large the input string grows, the memory footprint remains capped at a constant 26 elements, making the space complexity `O(1)`.