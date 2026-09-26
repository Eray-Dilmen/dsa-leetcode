# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# 1. Optimal Solution (Fast and Slow Pointers / One-Pass)
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next


# 2. Brute Force Solution (Length Check / Two-Pass)
class SolutionBruteForce:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        curr = head
        lenn = 0
        while curr:
            lenn += 1
            curr = curr.next

        if lenn == n:
            return head.next

        curr = head

        for i in range(0, lenn - n - 1):
            curr = curr.next

        curr.next = curr.next.next
        return head