class Solution(object):
    def check(self, nums):
        c=0
        for i in range(len(nums)):
            if nums[(i+1)%len(nums)]<nums[i]:
                c+=1
        if c==0 or c==1:
            return True
        else:
            return False


        