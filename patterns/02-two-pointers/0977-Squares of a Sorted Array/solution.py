# 1. Two Pointers & Reverse Approach (Optimal)
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        left = 0
        right = len(nums) - 1
        result = []

        while left <= right:
            if nums[left] ** 2 > nums[right] ** 2:
                result.append(nums[left] ** 2)
                left += 1
            else:
                result.append(nums[right] ** 2)
                right -= 1

        result.reverse()
        return result


# 2. Squaring and Sorting Approach (Alternative / Brute Force)
class SolutionSorting:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        nums.sort()
        return nums