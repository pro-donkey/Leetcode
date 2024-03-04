class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        mx_score = 0
        score = 0
        left = 0
        right = n - 1
        tokens.sort()
        while left <= right:
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                mx_score = max(mx_score,score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            
            else :
                break
        
        return mx_score
