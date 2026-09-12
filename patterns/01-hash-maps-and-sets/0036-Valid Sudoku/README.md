> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)


Determine if a `9 x 9` Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits `1-9` without repetition.
2. Each column must contain the digits `1-9` without repetition.
3. Each of the nine `3 x 3` sub-boxes of the grid must contain the digits `1-9` without repetition.

Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable. Only the filled cells need to be validated according to the mentioned rules.

### Example 1:
> **Input:** board = 
> [["5","3",".",".","7",".",".",".","."]
> ,["6",".",".","1","9","5",".",".","."]
> ,[".","9","8",".",".",".",".","6","."]
> ,["8",".",".",".","6",".",".",".","3"]
> ,["4",".",".","8",".","3",".",".","1"]
> ,["7",".",".",".","2",".",".",".","6"]
> ,[".","6",".",".",".",".","2","8","."]
> ,[".",".",".","4","1","9",".",".","5"]
> ,[".",".",".",".","8",".",".","7","9"]]
>  
> **Output:** `true`  

### Example 2:
> **Input:** board = 
> [["8","3",".",".","7",".",".",".","."]
> ,["6",".",".","1","9","5",".",".","."]
> ,[".","9","8",".",".",".",".","6","."]
> ,["8",".",".",".","6",".",".",".","3"]
> ,["4",".",".","8",".","3",".",".","1"]
> ,["7",".",".",".","2",".",".",".","6"]
> ,[".","6",".",".",".",".","2","8","."]
> ,[".",".",".","4","1","9",".",".","5"]
> ,[".",".",".",".","8",".",".","7","9"]]
>  
> **Output:** `false`  
> **Explanation:** Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.  

> ⚠️ **Crucial Performance Note: `list` vs `set`**
> 
> * `x in list` $\rightarrow O(n)$: A list is a sequential array structure. Python checks elements one by one from start to finish (linear search). If the element is at the end or not in the list, it scans every single item.
> * `x in set` $\rightarrow O(1)$: A `set` uses a **hash table** under the hood. The hash value of the searched element is calculated directly, and its position in the table is checked in a single step (average case). 

---

### 1. Hash Set Approach (Optimal)

We validate the board by doing 3 separate passes: one for rows, one for columns, and one for the 3x3 sub-boxes. To ensure there are no duplicates, we use a Hash Set. Because looking up an item in a set takes `O(1)` time, this operation is highly efficient.

```python
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # row validation
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)

        # column validation
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
                    
        # box validation
        starts = [(0,0),(0,3),(0,6),
                  (3,0),(3,3),(3,6),
                  (6,0),(6,3),(6,6)]

        for i,j in starts:
            s = set()
            for row in range(i,i+3):
                for column in range(j,j+3):
                    item = board[row][column]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True
```

**Time Complexity:** `O(1)`

Since the board size is strictly fixed at `9x9`, iterating over it takes a constant `81` operations per pass. The set lookup is `O(1)`. Thus, the time complexity is `O(1)` (or `O(N^2)` if `N` was variable, but it is not).

**Space Complexity:** `O(1)`

The set will hold at most 9 elements at any given time. This requires a constant amount of extra memory.

--- 

### 2. List Lookup Approach (Inefficient / Brute Force)

If we use a `list` instead of a `set` to track seen elements, the algorithm will perform a linear search (`O(n)`) every time we check `if item in l`. While a 9x9 board is too small for this to cause a Time Limit Exceeded (TLE) error, this logic becomes a massive bottleneck in standard algorithms.

```python
class SolutionBruteForce:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Using a List instead of a Set triggers O(n) linear search lookups
        for i in range(9):
            l = []
            for j in range(9):
                item = board[i][j]
                if item in l:
                    return False
                elif item != '.':
                    l.append(item)
                    
        # (Assuming the same logic is repeated for columns and boxes using lists)
        return True
```

**Time Complexity:** `O(1)`

Technically still constant due to the fixed 9x9 board, but fundamentally slower by a constant factor because of `O(n)` linear lookups instead of `O(1)` hash lookups.

**Space Complexity:** `O(1)`

Lists also require a constant amount of memory bounded by 9 elements.