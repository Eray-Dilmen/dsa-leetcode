> 💡 **Note:** This problem is solved using the **2D Prefix Sum** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [1314. Matrix Block Sum](https://leetcode.com/problems/matrix-block-sum/)

Given an `m x n` matrix `mat` and an integer `k`, return a matrix `answer` where each `answer[i][j]` is the sum of all elements `mat[r][c]` for:
* $i - k \le r \le i + k$
* $j - k \le c \le j + k$
* $(r, c)$ is a valid position in the matrix.

### Example 1:
> **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1`
> **Output:** `[[12,21,16],[27,45,33],[24,39,28]]`

### Example 2:
> **Input:** `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2`
> **Output:** `[[45,45,45],[45,45,45],[45,45,45]]`

---

### 1. 2D Prefix Sum Approach (Optimal)

* Calculating the block sum for every single cell independently requires repeated addition of the same overlapping regions. To optimize this, we compute a **2D Prefix Sum** matrix first.
* We pad the prefix sum matrix with an extra row and column (making it `(m+1) x (n+1)`). This avoids out-of-bounds indexing errors when checking the top ($i-1$) and left ($j-1$) neighbors for the very first row and column.
* The size of the block we are summing expands `k` units in all four directions. This creates a bounding box of size $(2k + 1) \times (2k + 1)$ around the center element.
* Once the 2D Prefix Sum matrix is built, the sum of any rectangular submatrix defined by top-left `(r1, c1)` and bottom-right `(r2, c2)` can be found in $O(1)$ time using the inclusion-exclusion principle: 
  `Sum = Prefix[r2][c2] - Prefix[r1-1][c2] - Prefix[r2][c1-1] + Prefix[r1-1][c1-1]`.
* We carefully bound `r1, c1, r2, c2` to ensure they do not exceed the actual matrix dimensions using `max()` and `min()`.

```python
class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        
        prefix = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]
                
        answer = [[0] * n for _ in range(m)]
          
        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)
                
                r1 += 1
                c1 += 1
                r2 += 1
                c2 += 1
                
                answer[i][j] = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]
                
        return answer
```

**Time Complexity:** `O(m * n)`

Building the prefix sum matrix requires visiting each cell once, taking `O(m * n)`. Calculating the target sum for each of the `m * n` cells using the prefix array takes `O(1)` time per cell. The overall time complexity remains strictly linear with respect to the number of elements in the matrix.

**Space Complexity:** `O(m * n)`

We allocate an additional `(m+1) x (n+1)` matrix to store the prefix sums, as well as an `m x n` matrix for the answer.

--- 

### 2. Nested Loops / Bounding Box (Brute Force)

* For every cell `(i, j)` in the matrix, we calculate its bounding box coordinates `r1, r2, c1, c2`. 
* We then use two nested loops to iterate through every single element inside that bounding box and accumulate the sum.
* This approach recalculates overlapping blocks constantly, leading to severe performance degradation on large matrices.

```python
class SolutionBruteForce:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        answer = []

        for i in range(m):
            row = []
            for j in range(n):
                r1, r2 = max(0, i - k), min(m - 1, i + k)
                c1, c2 = max(0, j - k), min(n - 1, j + k)
                
                total = 0
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        total += mat[r][c]
                
                row.append(total)
            answer.append(row)
            
        return answer
```

**Time Complexity:** `O(m * n * k^2)`

For each of the `m * n` elements, we iterate through a block of size up to $(2k + 1) \times (2k + 1)$. This gives a time complexity heavily dependent on `k`.

**Space Complexity:** `O(m * n)`

We allocate the `answer` matrix to store the results.