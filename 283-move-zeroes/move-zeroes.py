class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        f=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                f.append(nums[i])
        while len(f)<len(nums):
            f.append(0)
        nums[:]=f

