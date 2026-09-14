# Optimal Solution
class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        freq = {0: 1}

        for num in nums:
            prefix_sum += num

            if prefix_sum - k in freq:
                count += freq[prefix_sum - k]

            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1

        return count


# Brute Force Solution (Time Limit Exceeded)
class SolutionBruteForce:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0
        for l in range(len(nums)):
            summ = 0
            for r in range(l, len(nums)):
                summ += nums[r]
                if summ == k:
                    count += 1
        return count