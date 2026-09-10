# 1. Sorting & Two Pointers Approach (Optimal)
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        answer = []
        nums.sort()

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                lo, hi = j + 1, n - 1
                while lo < hi:
                    summ = nums[i] + nums[j] + nums[lo] + nums[hi]

                    if summ == target:
                        answer.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        hi -= 1

                        while lo < hi and nums[lo] == nums[lo - 1]:
                            lo += 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1

                    elif summ < target:
                        lo += 1
                    else:
                        hi -= 1

        return answer


# 2. Brute Force Approach (Time Limit Exceeded)
class SolutionBruteForce:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        unique_quads = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n):
                        if nums[i] + nums[j] + nums[k] + nums[l] == target:
                            quad = tuple(sorted((nums[i], nums[j], nums[k], nums[l])))
                            unique_quads.add(quad)

        return [list(q) for q in unique_quads]