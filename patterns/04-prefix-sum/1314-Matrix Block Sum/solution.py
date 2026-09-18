# Optimal Solution
class Solution:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])

        prefix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

        answer = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                r1 = max(0, i - k)
                c1 = max(0, j - k)
                r2 = min(m - 1, i + k)
                c2 = min(n - 1, j + k)

                r1 += 1
                c1 += 1
                r2 += 1
                c2 += 1

                answer[i][j] = prefix[r2][c2] - prefix[r1 - 1][c2] - prefix[r2][c1 - 1] + prefix[r1 - 1][c1 - 1]

        return answer


# Brute Force Solution
class SolutionBruteForce:
    def matrixBlockSum(self, mat: list[list[int]], k: int) -> list[list[int]]:
        m, n = len(mat), len(mat[0])
        answer = []

        for i in range(m):
            row = []
            for j in range(n):
                r1, r2 = max(0, i - k), min(m - 1, i + k)
                c1, c2 = max(0, j - k), min(n - 1, j + k)

                total = 0
                for r in range(r1, r2 + 1):
                    for c in range(c1, c2 + 1):
                        total += mat[r][c]

                row.append(total)
            answer.append(row)

        return answer