# Optimal Solution
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l = 0
        max_avg = float('-inf')
        summ = 0

        for r in range(len(nums)):
            summ += nums[r]

            if (r - l + 1) == k:
                avg = summ / k
                max_avg = max(max_avg, avg)
                summ -= nums[l]
                l += 1

        return max_avg


# Brute Force Solution
class SolutionBruteForce:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        max_avg = float('-inf')
        n = len(nums)

        for i in range(n - k + 1):
            summ = sum(nums[i:i + k])
            avg = summ / k
            max_avg = max(max_avg, avg)

        return max_avg