# 1. Two Pointers Approach (Optimal)
class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            w = right - left
            h = min(height[left], height[right])
            a = w * h
            max_area = max(max_area, a)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# 2. Brute Force Approach (Time Limit Exceeded)
class SolutionBruteForce:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                w = j - i
                h = min(height[i], height[j])
                max_area = max(max_area, w * h)

        return max_area