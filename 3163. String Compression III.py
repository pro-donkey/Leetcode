class Solution:
    def compressedString(self, word: str) -> str:
        freq = []
        cnt, n, char = 1, len(word), word[0]
        for i in range(1, n):
            if char == word[i] and cnt < 9:
                cnt += 1
            else:
                freq.append(str(cnt))
                freq.append(char)
                cnt = 1
                char = word[i]

        if cnt > 1:
            freq.append(str(cnt))
            freq.append(word[-1])
        else:
            freq.append(str(1))
            freq.append(word[-1])
        ans = "".join(freq)
        return ans
