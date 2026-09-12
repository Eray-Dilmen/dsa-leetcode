# Optimal
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        longest = 0
        sett = set()

        for r in range(len(s)):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            w = r - l + 1
            longest = max(longest, w)
            sett.add(s[r])

        return longest


# Brute Force
class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_len = 0
        n = len(s)

        for i in range(n):
            seen = set()
            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                max_len = max(max_len, j - i + 1)

        return max_len