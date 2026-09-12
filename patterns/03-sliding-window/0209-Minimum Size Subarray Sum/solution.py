# Optimal
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minn = float('inf')
        summ = 0
        l = 0

        for r in range(len(nums)):
            summ += nums[r]

            while summ >= target:
                minn = min(minn, r - l + 1)
                summ -= nums[l]
                l += 1

        return minn if minn != float('inf') else 0


# Brute Force
class SolutionBruteForce:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        minn = float('inf')
        n = len(nums)

        for i in range(n):
            summ = 0
            for j in range(i, n):
                summ += nums[j]
                if summ >= target:
                    minn = min(minn, j - i + 1)
                    break

        return minn if minn != float('inf') else 0