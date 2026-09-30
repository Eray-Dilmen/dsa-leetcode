class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        ans = 0
        while prev:
            ans = max(ans, head.val + prev.val)
            head = head.next
            prev = prev.next

        return ans


class SolutionAlternative:
    def pairSum(self, head: Optional[ListNode]) -> int:
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