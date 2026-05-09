class Solution(object):
    def removeDuplicates(self, nums):
        f=[nums[0]]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                f.append(nums[i])
        nums[:]=f
        return len(f)
        