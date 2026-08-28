class Solution(object):
    def moveZeroes(self, nums):
        f=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                f.append(nums[i])
        while len(f)<len(nums):
            f.append(0)
        nums[:]=f


