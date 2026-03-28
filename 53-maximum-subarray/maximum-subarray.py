class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum=nums[0]
        curr=nums[0]
        for i in range(1,len(nums)):
            curr=max(nums[i],curr+nums[i])
            max_sum=max(max_sum,curr)
        return max_sum

        
                



