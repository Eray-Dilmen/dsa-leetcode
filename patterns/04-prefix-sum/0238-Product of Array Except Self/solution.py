# Optimal Solution
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)
        ans[0] = 1

        for i in range(1, len(nums)):
            ans[i] = ans[i - 1] * nums[i - 1]

        rightProduct = 1

        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= rightProduct
            rightProduct *= nums[i]

        return ans


# Brute Force Solution 1 (Nested Loops)
class SolutionBruteForce1:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)

        for i in range(len(nums)):
            summ = 1
            for j in range(len(nums)):
                if j == i:
                    continue
                summ *= nums[j]

            ans[i] = summ

        return ans


# Brute Force Solution 2 (Two-Sided While Loops)
class SolutionBruteForce2:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        ans = [0] * len(nums)

        for i in range(len(nums)):
            prefix = 0
            summ = 1
            suffix = len(nums) - 1

            while prefix < i:
                summ *= nums[prefix]
                prefix += 1

            while suffix > i:
                summ *= nums[suffix]
                suffix -= 1

            ans[i] = summ

        return ans