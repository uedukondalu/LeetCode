class Solution(object):
    def removeElement(self, nums, val):
        f=0
        for i in range(len(nums)):
            if nums[i]!=val:
                nums[f]=nums[i]
                f+=1
        return f
        