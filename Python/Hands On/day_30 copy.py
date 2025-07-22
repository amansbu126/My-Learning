nums=[0,0,1,1,1,2,2,3,3,4]
k = nums[0]

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[k] = nums[i]
        k += 1

print(k)
print(nums[:k])

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        
        return i + 1

# Example usage
nums = [0, 0, 1, 1, 2, 3, 3]
solution = Solution()
k = solution.removeDuplicates(nums)

print("Number of unique elements:", k)
print("Updated array:", nums[:k])


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        i=0
        j=i+1
        while j<len(nums):
            if nums[i]!=nums[j]:
               nums[k]= nums[j]
               i+=1
               k+=1
            j+=1
        return k
    
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[j - 1]:
                nums[i] = nums[j]
                i += 1

        return i  # Correct indentation

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        nums[0]=nums[0]
        for n in range(1,len(nums)):
            if nums[n-1]==nums[n]:
                continue
            else:
                nums[i]=nums[n]
                i+=1
        return i