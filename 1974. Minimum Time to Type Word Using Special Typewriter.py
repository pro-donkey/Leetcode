class Solution:
    def minTimeToType(self, word: str) -> int:
        time = 0
        n = len(word)
        word = "a" + word
        for i in range(1, n + 1):
            front = abs(ord(word[i]) - ord(word[i - 1]))
            back = 26 - front
            time += min(front, back)

        time += n
        return time
