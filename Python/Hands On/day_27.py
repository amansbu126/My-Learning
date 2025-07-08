class Solution:
    def Isogram_Check(self, s):
        # Code here
        val1=''
        val2=''
        res=0
        for i in range(len(s)):
            val1=s[i]
            for j in range(i+1,len(s)):
                val2=s[j]
                if val1==val2:
                    res+=1
        if res==1:
            return 0
        else:
            return 1

# Creating an object of Solution
obj=Solution()

# Calling the convertFive method
print(obj.Isogram_Check('manishh'))