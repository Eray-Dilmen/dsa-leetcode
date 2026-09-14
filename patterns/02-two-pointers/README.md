> 📌 **Guide:** This directory serves as a Concept Map for the **Two Pointers** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0167-Two Sum II - Input Array Is Sorted`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Two Pointers Pattern?

* **Definition:** An algorithmic technique that uses two (or sometimes three) variables to iterate through a data structure simultaneously. 
* **The Core Superpower:** It optimizes algorithms by replacing nested loops (`O(n²)`) with a single concurrent pass (`O(n)`). Crucially, it achieves this while maintaining a strict `O(1)` space complexity because it only requires integer variables, completely avoiding extra memory allocation.

---

## Core Variations & Algorithmic Strategies

The "Two Pointers" pattern is not a single strict rule; it has several specialized sub-variations depending on the problem's objective.

### 1. Opposite Ends (Left & Right Pointers)
* **Algorithm:** Place one pointer at the start (`left = 0`) and another at the end (`right = len - 1`) of the array. Evaluate the condition, then move the pointers inward (e.g., `left += 1` or `right -= 1`) until they meet (`while left < right`).
* **When to use it:** Finding pairs in a **sorted** array, checking symmetry (palindromes), or comparing extremes.
* **Key Requirement:** For sum/search problems, the array **must** be sorted.
* **Repository Examples:**
  * [0167-Two Sum II - Input Array Is Sorted](./0167-Two%20Sum%20II%20-%20Input%20Array%20Is%20Sorted)
  * [0125-Valid Palindrome](./0125-Valid%20Palindrome)
  * [0011-Container With Most Water](./0011-Container%20With%20Most%20Water)

### 2. Same Direction (Reader / Writer Pointers)

* **Algorithm:** Both pointers start at index `0`. The `reader` (fast) pointer iterates through the array at every step to scan elements. The `writer` (slow) pointer only advances when a specific condition is met, overwriting or placing the next valid element.
* **When to use it:** In-place array modification (e.g., removing duplicates, shifting zeroes, filtering elements) without extra memory.
* **Difference from Pattern 05:** Here, the slow pointer advances **conditionally** based on values, and the goal is array mutation. In Pattern 05 (Fast & Slow / Floyd's), pointers move at **fixed, constant speeds** (1x vs 2x) to detect cycles or find midpoints.
* **Repository Examples:**
  * [0026-Remove Duplicates from Sorted Array](./0026-Remove%20Duplicates%20from%20Sorted%20Array)
  * [0283-Move Zeroes](./0283-Move%20Zeroes)

### 3. Pivot + Two Pointers (3Sum / k-Sum)
* **Algorithm:** When you need to find a triplet, combining an outer loop with inner Two Pointers reduces the complexity from `O(n³)` to `O(n²)`. Fix one element using a `for` loop (the pivot), and use the **Opposite Ends** technique for the remaining subarray to find the other two elements.
* **When to use it:** Finding triplets or quadruplets that sum to a specific target.
* **Repository Examples:**
  * [0015-3Sum](./0015-3Sum)

### 4. Partitioning / Three Pointers (Dutch National Flag)
* **Algorithm:** Used to segregate an array into three distinct zones (e.g., 0s, 1s, and 2s). It uses three pointers: `low` tracks the boundary of the first group, `high` tracks the boundary of the third group, and `mid` scans the array. Elements are swapped in-place, achieving `O(n)` time and `O(1)` space in a single pass.
* **When to use it:** Sorting arrays with a highly limited set of distinct values without using library sort functions.
* **Repository Examples:**
  * [0075-Sort Colors](./0075-Sort%20Colors)

---

## 💡 Professional Details & Edge Cases

* **Index Out of Bounds:** Always ensure your loop conditions (e.g., `while left < right` or `while mid <= high`) strictly prevent pointers from crossing improperly or accessing negative indices.
* **Avoiding Duplicates:** When dealing with combinations (like 3Sum), you can avoid processing the same value twice by skipping adjacent identical numbers (`if nums[i] == nums[i-1]: continue`). This bypasses the need for an `O(n)` linear search to check for duplicates.