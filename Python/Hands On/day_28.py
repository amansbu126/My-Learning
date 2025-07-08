class Solution:
    def Odd_Char_Deletion(self, s):
        # Code here
        new=''
        for i in range(len(s)):
            if i%2==0:
                new+=s[i]
        return new

# Creating an object of Solution
obj=Solution()

# Calling the convertFive method
print(obj.Odd_Char_Deletion('manishh'))