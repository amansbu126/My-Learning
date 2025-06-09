class Solution:
    def modify(self, s):
        # code here
        res=''
        if s[0].islower():
            return s.lower()
        elif s[0].isupper():
            return s.upper()
        

# Creating an object of Solution
obj1=Solution()
obj2=Solution()

# Calling the modify method
print(obj1.modify('Abcd'))
print(obj2.modify('aCCd'))