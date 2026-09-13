# Optimal Solution
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        letters_1 = {}
        letters_2 = {}

        for l in s1:
            letters_1[l] = letters_1.get(l, 0) + 1

        l = 0
        for r in range(len(s2)):
            letters_2[s2[r]] = letters_2.get(s2[r], 0) + 1

            if (r - l + 1) == len(s1):
                if letters_1 == letters_2:
                    return True

                letters_2[s2[l]] -= 1
                if letters_2[s2[l]] == 0:
                    del letters_2[s2[l]]
                l += 1

        return False


# Brute Force Solution
class SolutionBruteForce:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        sorted_s1 = sorted(s1)

        for i in range(m - n + 1):
            if sorted(s2[i:i + n]) == sorted_s1:
                return True

        return False