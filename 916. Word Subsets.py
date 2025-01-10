class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mp = {}
        for word in words2:
            counter = Counter(word)
            for val, cnt in counter.items():
                if val in mp:
                    if cnt > mp[val]:
                        mp[val] = cnt

                else:
                    mp[val] = cnt

        ans = []
        for word in words1:
            counter = Counter(word)
            flag = True
            for val, cnt in mp.items():
                if val in counter:
                    if counter[val] < cnt:
                        flag = False
                        break
                else:
                    flag = False
                    break

            if flag:
                ans.append(word)

        return ans
