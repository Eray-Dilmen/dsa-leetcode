# Optimal Solution (Prefix Sum Math Trick)
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0

        for index, val in enumerate(nums):
            right_sum = total_sum - left_sum - val

            if left_sum == right_sum:
                return index

            left_sum += val

        return -1


# Brute Force Solution (Two While Loops)
class SolutionBruteForce:
    def pivotIndex(self, nums: list[int]) -> int:
        for index, val in enumerate(nums):
            left = 0
            right = len(nums) - 1
            left_sum = 0
            right_sum = 0

            while left < index:
                left_sum += nums[left]
                left += 1

            while index < right:
                right_sum += nums[right]
                right -= 1

            if right_sum == left_sum:
                return index

        return -1