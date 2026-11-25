class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = nums[0]
        curr = nums[0]
        for num in nums[1:]:
            curr = max(num,num+curr)
            best = max(best, curr)
        return best
        
