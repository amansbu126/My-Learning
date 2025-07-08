class Solution:
    def Isogram_Check(self, s):
        # Code here
        res={}
        for char in s:
            if char in res:
                return 0
            else:
                res[char]=1
        return 1

# Creating an object of Solution
obj=Solution()

# Calling the convertFive method
print(obj.Isogram_Check('manishh'))