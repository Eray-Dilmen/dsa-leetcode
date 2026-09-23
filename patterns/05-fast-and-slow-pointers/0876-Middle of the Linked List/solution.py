# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Optimal Solution (Fast and Slow Pointers / One Pass)
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        slow = head
        fast = head

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        return slow


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# Brute Force Solution (Two Passes: Length + Iterate)
class SolutionBruteForce:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        lenght = 0

        curr = head

        while (curr):
            lenght += 1
            curr = curr.next

        middle = lenght // 2  # tam sayı bölmesi

        curr = head

        for i in range(0, middle):
            curr = curr.next

        return curr