class Solution:
  def twoSum(self,nums:list[int],target:int):
    if not nums:
        return 0
    
    sum=0

    for i in range(len(nums)):
        sum+=nums[i]
        return i
        if sum==target:
            break
        
# Test the function
nums = [2,7,11,15]
target=9
solution = Solution()
k = solution.twoSum(nums,target)
print(k)