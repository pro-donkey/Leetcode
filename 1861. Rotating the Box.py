class Solution:
    def rotateTheBox(self, boxGrid):
        n = len(boxGrid)
        m = len(boxGrid[0])

        ans = [['.'] * m for _ in range(n)]

        for r in range(n):
            cnt = 0

            for c in range(m):

                if boxGrid[r][c] == '#':
                    cnt += 1

                elif boxGrid[r][c] == '*':
                    ans[r][c] = '*'

                    for k in range(c - cnt, c):
                        ans[r][k] = '#'

                    cnt = 0

            for k in range(m - cnt, m):
                ans[r][k] = '#'

        ans = [list(row) for row in zip(*ans[::-1])]

        return ans
