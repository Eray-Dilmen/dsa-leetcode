# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. Optimal Solution (Fast and Slow Pointers)
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


# 2. Alternative Solution (Hash Set)
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


# 3. Brute Force Solution (Nested Loops with Indices)
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