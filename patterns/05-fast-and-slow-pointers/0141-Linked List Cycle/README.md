> 💡 **Note:** This problem is optimally solved using the **Fast and Slow Pointers** pattern. For the general logic, use cases, and theoretical details of this pattern, refer to the [pattern README.md](../README.md).

# [0141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)

Given `head`, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the `next` pointer. Internally, `pos` is used to denote the index of the node that tail's `next` pointer is connected to. **Note that `pos` is not passed as a parameter.**

Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

### Example 1:
> **Input:** `head = [3,2,0,-4], pos = 1`  
> **Output:** `true`  
> **Explanation:** There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

### Example 2:
> **Input:** `head = [1,2], pos = 0`  
> **Output:** `true`  
> **Explanation:** There is a cycle in the linked list, where the tail connects to the 0th node.

### Example 3:
> **Input:** `head = [1], pos = -1`  
> **Output:** `false`  
> **Explanation:** There is no cycle in the linked list.

---

### 1. Fast and Slow Pointers Approach (Optimal)

The most efficient way to detect a cycle in a linked list is using Floyd's Cycle-Finding Algorithm, commonly known as the Fast and Slow Pointers technique. 

**The Core Logic:**
We initialize two pointers, `slow` and `fast`, both starting at the `head`. The `slow` pointer moves one step at a time, while the `fast` pointer moves two steps at a time. If the linked list has no cycle, the `fast` pointer will eventually reach the end of the list (`None`). However, if there is a cycle, the `fast` pointer will eventually loop around and meet the `slow` pointer at the exact same node. 

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
                
        return False
```

**Time Complexity:** `O(N)`  
In the worst-case scenario (where a cycle exists), the fast pointer will catch up to the slow pointer in linear time. If there is no cycle, it reaches the end in $N/2$ steps.

**Space Complexity:** `O(1)`  
Only two pointers are used, requiring constant extra space.

--- 

### 2. Hash Set Approach (Alternative)

A simpler but less space-efficient way to check for a cycle is to keep track of every node we visit using a Hash Set. 

**The Core Logic:**
As we traverse the linked list, we check if the current node already exists in our `sett`. If there is no cycle, the loop will simply continue until it reaches `null` (the end of the list) and return `False`. If there is a cycle, we will eventually encounter a node that is already inside our set, at which point we immediately return `True`, breaking out of the loop.

```python
class SolutionHashSet:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        sett = set()
        
        while(curr):
            if curr in sett:
                return True
            sett.add(curr)
            curr = curr.next
            
        return False
```

**Time Complexity:** `O(N)`  
We traverse the list once. Set lookups and insertions take `O(1)` time on average.

**Space Complexity:** `O(N)`  
We store every single node in the Hash Set, which scales linearly with the size of the linked list.

---

### 3. Nested Loops Approach (Brute Force)

This is the most inefficient method, manually checking if any subsequent node points back to a previously visited node.

**Why do we use indices here?**
In a singly linked list, we can only move forward. We cannot easily check "have I seen this node before?" without extra memory (like a Hash Set). To solve this purely with pointers, we use `outer_index` and `inner_index` to restrict our inner loop. The inner loop only checks nodes starting from the `head` up to the current `outer` node. If the `outer.next` pointer matches any of these previously visited `inner` nodes, it confirms a backward link, meaning a cycle exists.

```python
class SolutionBruteForce:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        outer = head
        outer_index = 0
        
        while outer:
            inner = head
            inner_index = 0
            
            while inner_index < outer_index:
                if inner == outer.next:
                    return True
                inner = inner.next
                inner_index += 1
                
            outer = outer.next
            outer_index += 1
            
        return False
```

**Time Complexity:** `O(N^2)`  
For every node `outer` visits, the `inner` loop traverses from the beginning of the list up to that node, leading to a quadratic number of operations.

**Space Complexity:** `O(1)`  
We only use a few tracking variables (`outer`, `inner`, `outer_index`, `inner_index`).