> 📌 **Guide:** This directory serves as a Concept Map for the **Fast & Slow Pointers (Floyd's Tortoise and Hare)** pattern.
> * **Theoretical Logic:** Read this `README.md` for core principles, sub-variations, and time/space complexity analysis.
> * **Practical Problems:** Navigate to the specific problem folders (e.g., `0141-Linked List Cycle`) to see the pattern in action. Specific edge cases and alternative solutions are documented inside those folders.

## What is the Fast & Slow Pointers Pattern?

* **Definition:** Also known as Floyd’s Cycle Finding Algorithm, this pattern uses two pointers moving through a sequence at **different, constant speeds** (usually the slow pointer moves 1 step, and the fast pointer moves 2 steps).
* **The Core Superpower:** It solves problems on Linked Lists (and state-machine arrays) in `O(n)` time and `O(1)` space. 
* **Key Difference from Pattern 02 (Two Pointers):** 
  * In **Pattern 02 (Same Direction)**, the slow pointer moves *conditionally* (Reader/Writer) to modify an array in-place.
  * In **Pattern 05 (Floyd's Algorithm)**, both pointers move at *fixed relative speeds* (1 step vs. 2 steps) regardless of element values, specifically to detect cycles (infinite loops) or locate structural positions (like the midpoint) without extra memory.

---

## Core Variations & Algorithmic Strategies

This pattern heavily relies on mathematical inevitability: if two runners are on a circular track and one runs twice as fast as the other, the faster runner will eventually lap and catch up to the slower runner.

### 1. Cycle Detection (Does it loop?)
* **Algorithm:** Initialize both `slow` and `fast` pointers at the `head`. In a `while` loop, move `slow` by 1 step (`slow = slow.next`) and `fast` by 2 steps (`fast = fast.next.next`). If the pointers ever point to the exact same node (`slow == fast`), a cycle exists. If `fast` reaches the end (`null`), there is no cycle.
* **When to use it:** When checking if a Linked List loops back on itself, or when verifying if a mathematical sequence gets stuck in an infinite loop.
* **Repository Examples:**
  * [0141-Linked List Cycle](./0141-Linked%20List%20Cycle)
  * [0202-Happy Number](./0202-Happy%20Number)

### 2. Finding the Middle of a Sequence
* **Algorithm:** Start both pointers at the `head`. Move `slow` by 1 step and `fast` by 2 steps. By the time the `fast` pointer reaches the very end of the sequence, the `slow` pointer will have traveled exactly half the distance, landing on the middle node.
* **When to use it:** When you need to split a Linked List in half (e.g., for Merge Sort on Linked Lists) or check if a Linked List is a palindrome by reversing the second half.
* **Repository Examples:**
  * [0876-Middle of the Linked List](./0876-Middle%20of%20the%20Linked%20List)
  * [0234-Palindrome Linked List](./0234-Palindrome%20Linked%20List)

### 3. Finding the Start of the Cycle
* **Algorithm:** This is a two-phase mathematical trick. First, use Cycle Detection. Once `slow` and `fast` meet, **do not** return. Instead, move one of the pointers back to the very beginning (`head`) of the sequence. Then, move **both** pointers at the same speed (1 step at a time). The exact node where they collide again is the entrance to the cycle.
* **When to use it:** When the problem asks you to return the specific node where the cycle begins, or when finding a duplicate number in an array without modifying the array and strictly using `O(1)` space.
* **Repository Examples:**
  * [0142-Linked List Cycle II](./0142-Linked%20List%20Cycle%20II)
  * [0287-Find the Duplicate Number](./0287-Find%20the%20Duplicate%20Number)

---

## 💡 Professional Details & Edge Cases

* **Null Pointer Exceptions (NPE):** The most common error is trying to access `fast.next.next` when `fast` or `fast.next` is already `null`. Always structure your `while` loop condition carefully: `while fast and fast.next:` (in Python) or `while (fast != null && fast.next != null)` (in Java/C++).
* **Even vs. Odd Lengths:** When finding the middle of a Linked List, the definition of "middle" changes depending on if the length is even or odd. If the length is even, there are two middle nodes. The standard `fast = head, slow = head` setup lands on the **second** middle node. If you need it to land on the **first** middle node, initialize `fast = head.next` instead.
* **Arrays as Linked Lists:** Problems like *Find the Duplicate Number* give you an array where values point to indices. You can treat the array `nums` exactly like a Linked List by saying `next_node = nums[current_node]`, allowing you to apply Floyd's algorithm on arrays.