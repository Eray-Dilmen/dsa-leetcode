> 💡 **Note:** This problem is solved using the **Hash Maps & Sets** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/)


Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

### Example 1:
> **Input:** `nums = [1,2,3,1]`  
> **Output:** `true`

### Example 2:
> **Input:** `nums = [1,2,3,4]`  
> **Output:** `false`

### Example 3:
> **Input:** `nums = [1,1,1,3,3,4,3,2,4,2]`  
> **Output:** `true`

> **Note:** The Hash Set pattern is used to check for existence in `O(1)` time. By inserting elements into a Set as we iterate, we can instantly detect if an element has been seen before, avoiding the need for nested `O(n^2)` loops.

---

### 1. Hash Set Approach (Optimal)

We use a Hash Set which allows for `O(1)` time complexity for lookups. As we iterate through the array and add elements to the set, we check if the element is already in the set. If it is, it means the element has appeared before, and we immediately return `True` (Early Exit).

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        numbers = set()
        
        for number in nums:
            if number in numbers:
                return True
            numbers.add(number)
            
        return False
```

**Time Complexity:** `O(n)`

In the worst-case scenario (no duplicates), the array is completely traversed once. Lookup operations in a Hash Set take `O(1)` time on average, resulting in an overall `O(n)` time complexity.

**Space Complexity:** `O(n)`

In the worst-case scenario, all unique elements are stored in the Hash Set, taking memory proportional to the size of the array.

---

### 2. Frequency Map Approach (Alternative)

We use a dictionary to count how many times each number appears in the array. Then, we iterate through the dictionary to check if any number has a frequency greater than 1.

```python
class SolutionFrequencyMap:
    def containsDuplicate(self, nums: list[int]) -> bool:
        number_count = {}
        
        for number in nums:
            if number not in number_count:
                number_count[number] = 1
            else:
                number_count[number] += 1
        
        for number in number_count:
            if number_count[number] > 1:
                return True
        
        return False
```

**Time Complexity:** `O(n)`

Populating the dictionary takes `O(n)` time. Iterating over the unique elements in the dictionary takes another `O(n)` time in the worst case. Total time is `O(2n)`, which simplifies to `O(n)`.

**Space Complexity:** `O(n)`

In the worst-case scenario, all unique numbers and their frequencies are stored in the dictionary. While asymptotically the same as the Hash Set, dictionaries store both keys and values, giving it a slightly larger memory footprint constant.

---

### 3. Brute Force Approach

We set up nested loops to compare each element with every subsequent element. If a match is found, we return `True`. This method uses no extra space but is extremely slow and will result in a **Time Limit Exceeded (TLE)** error for large arrays.

```python
class SolutionBruteForce:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
                    
        return False
```

**Time Complexity:** `O(n^2)`

The nested loops traverse the array approximately `n(n-1)/2` times.

**Space Complexity:** `O(1)`

No additional data structure is created.