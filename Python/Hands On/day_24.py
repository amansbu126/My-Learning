class Solution:
    def convertFive(self, n):
        # Code here
        str_n=str(n)
        res=''
        for char in str_n:
            if char=='0':
                res=res+'5'
            else:
                res=res+char
        return res

# Creating an object of Solution
obj=Solution()

# Calling the convertFive method
print(obj.convertFive(1500))