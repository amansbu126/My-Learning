from typing import List  # ✅ Import required for type hinting

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        k = nums[0]  # First unique item is already at index 0
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k

# Test the function
nums = [1, 1, 2]
solution = Solution()
k = solution.removeDuplicates(nums)

print("Number of unique elements:", k)         # Output: 2
print("Unique elements:", nums[:k])            # Output: [1, 2]
