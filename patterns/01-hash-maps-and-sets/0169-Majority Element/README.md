> 💡 **Note:** This problem is typically solved using the **Boyer-Moore Voting Algorithm** for `O(1)` space, or **Hash Maps** for `O(n)` space. For the general logic of Hash Maps, refer to the [pattern README.md](../README.md).

# [169. Majority Element](https://leetcode.com/problems/majority-element/)


Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.

### Example 1:
> **Input:** `nums = [3,2,3]`  
> **Output:** `3`

### Example 2:
> **Input:** `nums = [2,2,1,1,1,2,2]`  
> **Output:** `2`

---

### 1. Boyer-Moore Voting Algorithm Approach (Optimal)

**How does the logic work? (Why is O(1) Memory Enough?)**
The core logic relies on a "mutual annihilation" (cancellation) principle:

* By problem definition, the majority element occupies **more than half** of the array ($> n/2$).
* If we were to pair up the majority element with any other different element and "delete" them both from the array simultaneously, the majority element would still not be destroyed; because it outnumbers all other numbers combined.
* The algorithm simulates this as follows:
  * `ans`: The current candidate number.
  * `count`: The power (or health) of the candidate.
  * If you encounter the candidate itself, its power increases (`count += 1`).
  * If you encounter a different number, one of each destroys the other (`count -= 1`).
  * When the power drops to zero (`count == 0`), the new number you see becomes the new candidate.
* Ultimately, even if all other numbers decrement the majority number one by one, the majority element will definitely remain at the end due to its numerical superiority.

Since you only keep two simple variables (`ans` and `count`), you don't need any dictionary or list memory $\rightarrow$ **$O(1)$ Space**.

```python
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        # Space Complexity = O(1)
        ans = 0
        count = 0
        
        # Time Complexity = O(N)
        for num in nums:
            if count == 0:
                ans = num
                
            if ans == num:
                count += 1
            else:
                count -= 1
                
        return ans
```

**Time Complexity:** `O(N)`
We iterate through the array exactly once.

**Space Complexity:** `O(1)`
As explained above, only two variables are used.

--- 

### 2. Hash Map Approach (Alternative)

We can iterate through the array and store the frequency of each element in a dictionary (Hash Map). After populating the dictionary, we iterate through its keys and return the one whose count is strictly greater than `len(nums) / 2`.

```python
class SolutionHashMap:
    def majorityElement(self, nums: list[int]) -> int:
        # Space Complexity = O(N)
        d = {}
        
        # Time Complexity = O(N)
        for i in nums:
            if i not in d:
                d[i] = 1
            elif i in d:
                d[i] += 1
                
        for i in d:
            if d[i] > (len(nums) / 2):
                return i
```

**Time Complexity:** `O(N)`
Populating the dictionary takes `O(N)` time, and searching through it takes `O(N)` time.

**Space Complexity:** `O(N)`
In the worst case, the dictionary stores frequencies for `N` unique elements, requiring linear extra space.

---

### 3. Sorting Approach (Brute Force)

Since the majority element appears more than `n / 2` times, if we sort the array, the majority element will always occupy the middle index `n // 2`, regardless of whether it is the smallest or largest number in the array. 

```python
class SolutionSorting:
    def majorityElement(self, nums: list[int]) -> int:
        # Space Complexity = O(1) or O(N) depending on sort
        # Time Complexity = O(N log N)
        nums.sort()
        return nums[len(nums) // 2]
```

**Time Complexity:** `O(N log N)`
The built-in sorting function dictates the time complexity.

**Space Complexity:** `O(1)` or `O(N)`
Depending on the sorting algorithm used by the language under the hood.