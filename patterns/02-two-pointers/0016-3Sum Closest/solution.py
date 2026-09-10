# 1. Sorting & Two Pointers Approach (Optimal)
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo, hi = i + 1, n - 1
            while lo < hi:
                cur_sum = nums[i] + nums[lo] + nums[hi]

                if abs(cur_sum - target) < abs(closest_sum - target):
                    closest_sum = cur_sum

                if cur_sum == target:
                    return cur_sum
                elif cur_sum < target:
                    lo += 1
                else:
                    hi -= 1

        return closest_sum


# 2. Brute Force Approach (Alternative)
class SolutionBruteForce:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        closest_sum = float('inf')

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    cur_sum = nums[i] + nums[j] + nums[k]
                    if abs(cur_sum - target) < abs(closest_sum - target):
                        closest_sum = cur_sum

        return closest_sum