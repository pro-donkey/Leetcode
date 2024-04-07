class Solution:
    def checkValidString(self, s: str) -> bool:
        minimum_open = 0
        maximum_open = 0

        for char in s:
            if char == "(":
                minimum_open += 1
                maximum_open += 1
            elif char == ")":
                minimum_open -= 1
                maximum_open -= 1
            else:  
                minimum_open -= 1
                maximum_open += 1
            if maximum_open < 0:
                return False
            if minimum_open < 0:
                minimum_open = 0
        
        return minimum_open == 0
