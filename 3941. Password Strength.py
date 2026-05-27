class Solution:
    def passwordStrength(self, password: str) -> int:
        pa = set(password)
        strength = 0
        
        for char in pa:
            if char.islower():
                strength += 1
            elif char.isupper():
                strength += 2
            elif char.isdigit():
                strength += 3
            elif char in "!@#$":
                strength += 5
                
        return strength



# Brute Force should be first but i am too lazy 

class Solution:
    def passwordStrength(self, password: str) -> int:
        small = set()
        large = set()
        number = set()
        special = set()
        for val in password:
            if ord("a") <= ord(val) <= ord("z"):
                small.add(val)
            elif ord("A") <= ord(val) <= ord("Z"):
                large.add(val)
            elif ord("0") <= ord(val) <= ord("9"):
                number.add(val)
            else:
                special.add(val)

        return len(small) * 1 + len(large) * 2 + len(number) * 3 + len(special) * 5
