class Solution(object):
    def removeDuplicates(self, nums):
        f=[]
        for i in range(len(nums)):
            if nums[i] not in f:
                f.append(nums[i])
        nums[:]=f
        return len(f)
        