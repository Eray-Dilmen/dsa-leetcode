# 1. In-Place Two Pointers Approach (Optimal)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue

            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# 2. Array Filtering & Two Pointers (Alternative)
class SolutionAlternative:
    def isPalindrome(self, s: str) -> bool:
        nonalpha = []

        for i in range(len(s)):
            if s[i].isalnum():
                nonalpha.append(s[i].lower())

        left = 0
        right = len(nonalpha) - 1

        while left < right:
            if nonalpha[left] != nonalpha[right]:
                return False
            left += 1
            right -= 1

        return True


# 3. Built-in Reverse Approach (Brute Force)
class SolutionBruteForce:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]