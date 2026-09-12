# Optimal
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        longest = 0
        count = {}
        max_freq = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])

            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            longest = max(longest, (r - l + 1))

        return longest


# Brute Force
class SolutionBruteForce:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        n = len(s)

        for i in range(n):
            count = {}
            max_freq = 0
            for j in range(i, n):
                count[s[j]] = count.get(s[j], 0) + 1
                max_freq = max(max_freq, count[s[j]])

                if (j - i + 1) - max_freq <= k:
                    longest = max(longest, j - i + 1)
                else:
                    break

        return longest