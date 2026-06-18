class Solution(object):
    def sortColors(self, nums):
        f=[]
        g=[]
        j=[]
        for i in range(len(nums)):
            if nums[i]==0:
                f.append(nums[i])
            elif nums[i]==1:
                g.append(nums[i])
            else:
                j.append(nums[i])
        r=f+g+j
        nums[:]=r
        return nums