class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        
        while i < len(nums):
            j = nums[i]
            if j < len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i, n in enumerate(nums):
            if i != n:
                return i
        
        return len(nums)