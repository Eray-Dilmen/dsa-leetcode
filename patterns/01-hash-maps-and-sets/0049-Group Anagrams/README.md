> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)


Given an array of strings `strs`, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:
**Input:** `strs = ["eat","tea","tan","ate","nat","bat"]`  
**Output:** `[["bat"],["nat","tan"],["ate","eat","tea"]]`

### Example 2:
**Input:** `strs = [""]`  
**Output:** `[[""]]`

### Example 3:
**Input:** `strs = ["a"]`  
**Output:** `[["a"]]`

---

### 1. Frequency Tuple & Hash Map Approach (Optimal)

Instead of sorting the strings, we use a **character frequency array** as a unique signature (key) for each word. Anagrams will have the exact same character frequencies, meaning they will generate the exact same signature.

**Step-by-Step Logic:**
* **`defaultdict(list)`:** Normally, appending to a non-existent key in a dictionary throws a `KeyError`. `defaultdict(list)` means: *"If the key I'm looking for doesn't exist yet, don't throw an error; automatically create an empty list `[]` for it."*
* **`count = [0] * 26`:** Creates a list of 26 zeros representing the English alphabet. This resets for every new word and acts as the common signature.
* **`ord(c) - ord('a')`:** The `ord()` function returns the ASCII numerical value of a character (e.g., 'a'=97, 'b'=98). Subtracting `ord('a')` maps 'a' to index 0, 'b' to index 1, and 'z' to index 25. For example, if `c` is 'b': $98 - 97 = 1$. The code `count[1] += 1` increments the count for 'b'.
* **`key = tuple(count)`:** Lists (`[]`) are mutable in Python and cannot be used as dictionary keys. This line converts the frequency list into an immutable `tuple ()` structure.
* **`anagrams_dict[key].append(s)`:** Words like "eat", "tea", and "ate" will all produce the exact same tuple signature (e.g., `(1, 0, 0, 0, 1, ..., 1, ...)`). The dictionary goes to this shared signature key and appends the original word to its list.
* **`anagrams_dict.values()`:** We only need the grouped words. This returns just the grouped lists from the dictionary, ignoring the tuple keys.

```python
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Space Complexity = O(N * M)
        anagrams_dict = defaultdict(list)
        
        # Time Complexity = O(N * M)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
                
            key = tuple(count)
            anagrams_dict[key].append(s)
            
        return list(anagrams_dict.values())
```

**Time Complexity:** $O(N \cdot M)$
* $N$ is the total number of words. $M$ is the maximum length of a single word.
* The outer loop runs $N$ times. The inner loop reads each character of the word, taking $M$ steps.
* The `ord` calculation, adding to the array, and dictionary insertion are all $O(1)$ operations.
* Converting the 26-element array to a tuple takes $O(26) = O(1)$ constant time.
* Total time: $N \times O(M) = O(N \cdot M)$.

**Space Complexity:** $O(N \cdot M)$
* In the worst case (no words are anagrams), the dictionary will create $N$ separate groups.
* All original words are stored inside the dictionary's lists. The total size of all characters stored is at most $N \times M$.
* The 26-element tuple keys take up constant $O(1)$ space.
* Therefore, the total space occupied by the stored words is $O(N \cdot M)$.

--- 

### 2. Sorting Approach (Alternative / Slower)

If two words are anagrams, sorting them alphabetically will result in the exact same string (e.g., "eat" and "tea" both become "aet"). We can use this sorted string directly as the dictionary key. While the code is shorter, sorting every string adds a logarithmic time penalty, making it less optimal for very long words.

```python
from collections import defaultdict

class SolutionSorting:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Space Complexity = O(N * M)
        anagrams_dict = defaultdict(list)
        
        # Time Complexity = O(N * M log M)
        for s in strs:
            sorted_word = "".join(sorted(s))
            anagrams_dict[sorted_word].append(s)
            
        return list(anagrams_dict.values())
```

**Time Complexity:** $O(N \cdot M \log M)$
Sorting each word of length $M$ takes $O(M \log M)$ time. We do this for $N$ words.

**Space Complexity:** $O(N \cdot M)$
We still store all words in the dictionary.