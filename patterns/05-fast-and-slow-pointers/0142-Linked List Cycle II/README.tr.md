# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 1. Optimal Solution (Fast and Slow Pointers / Floyd's Cycle-Finding)
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                fast = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return fast

        return None


# 2. Brute Force Solution (Hash Set)
class SolutionHashSet:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sett = set()
        curr = head

        while(curr):
            if curr in sett:
                return curr

            sett.add(curr)
            curr = curr.next

        return None