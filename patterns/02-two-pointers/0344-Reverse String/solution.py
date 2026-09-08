# 1. Two Pointers Approach (Optimal)
class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0
        right = len(s) - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s


# 2. Built-in Method Approach (Alternative)
class SolutionAlternative:
    def reverseString(self, s: list[str]) -> None:
        s.reverse()
        return s