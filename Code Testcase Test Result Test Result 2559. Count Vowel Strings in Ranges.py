class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = set(["a", "e", "i", "o", "u"])
        pre = [0] * (len(words) + 1)
        for i in range(len(words)):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre[i + 1] = pre[i] + 1
            else:
                pre[i + 1] = pre[i]

        ans = []

        for query in queries:
            i, j = query[0], query[1]
            val = pre[j + 1] - pre[i]
            ans.append(val)

        return ans
