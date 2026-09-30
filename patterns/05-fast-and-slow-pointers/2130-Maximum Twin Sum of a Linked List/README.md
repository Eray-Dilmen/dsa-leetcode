> 💡 **Note:** This problem is optimally solved using the **Fast and Slow Pointers** pattern combined with **Reversing a Linked List**. For the theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [2130. Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

In a linked list of size `n`, where `n` is **even**, the `ith` node (0-indexed) of the linked list is known as the **twin** of the `(n-1-i)th` node, if `0 <= i <= (n / 2) - 1`.

* For example, if `n = 4`, then node `0` is the twin of node `3`, and node `1` is the twin of node `2`. These are the only nodes with twins for `n = 4`.

The **twin sum** is defined as the sum of a node and its twin.

Given the `head` of a linked list with even length, return the **maximum twin sum** of the linked list.

### Example 1:
> **Input:** `head = [5,4,2,1]`  
> **Output:** `6`  
> **Explanation:**  
> Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.  
> There are no other nodes with twins in the linked list.  
> Thus, the maximum twin sum of the linked list is 6.  

---

### 1. Fast & Slow Pointers and Reverse Approach (Optimal)

To achieve an $O(1)$ space complexity, we cannot use an external array to store the node values. Instead, we can manipulate the linked list itself to bring the twin nodes together. 

The optimal approach consists of three main steps:
1. **Find the Middle:** We use the Fast and Slow pointers technique. When the `fast` pointer reaches the end of the list, the `slow` pointer will be exactly at the start of the second half.
2. **Reverse the Second Half:** We reverse the pointers of the second half of the list (starting from `slow`). This makes the second half point backwards, allowing us to traverse it from the original tail towards the center.
3. **Calculate Twin Sums:** We traverse the first half (using `head`) and the reversed second half (using `prev`) simultaneously. Since they are now effectively converging towards the center, adding their values gives us the twin sums.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        
        # 1. Find the middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 2. Reverse the second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        # 3. Add from both ends to the center
        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next
            
        return ans
```

**Time Complexity:** `O(N)`  
We traverse the list to find the middle ($N/2$ steps), reverse the second half ($N/2$ steps), and calculate the sums ($N/2$ steps). The overall time is strictly linear.

**Space Complexity:** `O(1)`  
We only use a few pointer variables (`slow`, `fast`, `prev`, `nxt`), modifying the linked list in place without any extra data structures.

--- 

### 2. Array Conversion Approach (Alternative)

If space complexity is not a strict constraint, the simplest way to solve this is by converting the linked list into a standard array (list in Python). Once the values are in an array, we can easily access the twins using their indices.

**The Mathematical Boundary ($0 \le i \le (n/2) - 1$):**
Why do we iterate up to `n // 2`? This boundary ensures we only take indices from the first half of the array. 
* Since indices start at `0`, the first element is $i = 0$.
* Since the array has an even length, the exact last element of the first half is located at index $(n/2) - 1$.
This mathematical condition guarantees that we move from both ends towards the center without crossing over into the second half.

```python
class SolutionAlternative:
    def pairSum(self, head: ListNode | None) -> int:
        maxx = float('-inf')
        curr = head
        vals = []
        
        while curr:
            vals.append(curr.val)
            curr = curr.next
            
        n = len(vals)
        for i in range(n // 2):
            maxx = max(maxx, vals[i] + vals[n - 1 - i])
            
        return maxx
```

**Time Complexity:** `O(N)`  
We traverse the linked list once to build the array ($N$ steps), and then iterate through half of the array ($N/2$ steps) to find the maximum sum.

**Space Complexity:** `O(N)`  
We store all $N$ values of the linked list in a new array (`vals`), which requires linear extra space.