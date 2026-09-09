# 1. Two Pointers Approach (Optimal)
class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) - 1
        leftMax = height[l]
        rightMax = height[r]
        res = 0

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += max(0, leftMax - height[l])
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += max(0, rightMax - height[r])

        return res


# 2. Dynamic Programming / Prefix Arrays Approach (Alternative)
class SolutionAlternative:
    def trap(self, height: list[int]) -> int:
        l_wall = r_wall = 0
        n = len(height)
        max_left = [0] * n
        max_right = [0] * n

        for i in range(n):
            j = -i - 1
            max_left[i] = l_wall
            max_right[j] = r_wall
            l_wall = max(l_wall, height[i])
            r_wall = max(r_wall, height[j])

        summ = 0
        for i in range(n):
            pot = min(max_left[i], max_right[i])
            summ += max(0, pot - height[i])

        return summ


# 3. Brute Force Approach (Time Limit Exceeded)
class SolutionBruteForce:
    def trap(self, height: list[int]) -> int:
        res = 0
        n = len(height)

        for i in range(n):
            left_max = max(height[:i + 1]) if i >= 0 else 0
            right_max = max(height[i:]) if i < n else 0
            res += min(left_max, right_max) - height[i]

        return res