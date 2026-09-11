# Optimal
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Time Complexity: O(N)
        # Space Complexity: O(1)
        max_w = 0
        num_zeros = 0
        n = len(nums)
        l = 0

        for r in range(n):
            if nums[r] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[l] == 0:
                    num_zeros -= 1
                l += 1

            w = r - l + 1
            max_w = max(max_w, w)

        return max_w


# Brute Force
class SolutionBruteForce:
    def longestOnes(self, nums: list[int], k: int) -> int:
        # Time Complexity: O(N^2)
        # Space Complexity: O(1)
        max_w = 0
        n = len(nums)

        for i in range(n):
            num_zeros = 0
            for j in range(i, n):
                if nums[j] == 0:
                    num_zeros += 1
                if num_zeros > k:
                    break
                max_w = max(max_w, j - i + 1)

        return max_w