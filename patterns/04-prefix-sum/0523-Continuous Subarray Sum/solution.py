# Optimal Solution (Hash Map / Modulo)
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        remainder_map = {0: -1}
        summ = 0

        for index, val in enumerate(nums):
            summ += val
            rem = summ % k

            if rem in remainder_map:
                if index - remainder_map[rem] >= 2:
                    return True
            else:
                remainder_map[rem] = index

        return False


# Brute Force Solution (Nested Loops - TLE)
class SolutionBruteForce:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        for i in range(0, len(nums) - 1):
            summ = nums[i]
            for j in range(i + 1, len(nums)):
                summ += nums[j]
                if summ % k == 0:
                    return True

        return False