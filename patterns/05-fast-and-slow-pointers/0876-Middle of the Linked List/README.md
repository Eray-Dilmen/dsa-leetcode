> 💡 **Note:** This problem will be optimally solved using the **Fast and Slow Pointers** pattern. Currently, this file contains the naive two-pass approach. For the general logic, use cases, and theoretical details of the pointer patterns, refer to the [pattern README.md](../README.md).

# [0876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

Given the `head` of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the **second middle node**.

### Example 1:
> **Input:** `head = [1,2,3,4,5]`  
> **Output:** `[3,4,5]`  
> **Explanation:** The middle node of the list is node 3.

### Example 2:
> **Input:** `head = [1,2,3,4,5,6]`  
> **Output:** `[4,5,6]`  
> **Explanation:** Since the list has two middle nodes with values 3 and 4, we return the second one.

---

### 1. Find Length and Iterate Approach (Brute Force / Two Passes)

Since we cannot know the length of a singly linked list beforehand, the most straightforward approach is to traverse the entire list to count the total number of nodes. 

Once we have the total length, we calculate the index of the middle node by performing integer division (`length // 2`). We then reset our pointer back to the `head` and traverse the list a second time, stopping exactly at the calculated middle index.

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        lenght = 0
        
        curr = head
        
        while (curr):
            lenght += 1
            curr = curr.next
            
        middle = lenght//2 # tam sayı bölmesi
        
        curr = head
        
        for i in range(0, middle):
            curr = curr.next
            
        return curr
```

**Time Complexity:** `O(N)`  
We traverse the entire list once to find the length ($N$ steps), and then we traverse it again up to the middle ($N/2$ steps). The overall time complexity is $O(N)$, but it requires 1.5 passes over the data.

**Space Complexity:** `O(1)`  
We only use a few variables (`lenght`, `middle`, `curr`) to keep track of counts and nodes, requiring constant extra space.