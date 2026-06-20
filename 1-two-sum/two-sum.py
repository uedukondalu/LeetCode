class Solution(object):
    def twoSum(self, nums, target):
        n=nums
        t=target
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                if n[i]+n[j]==t:
                    return i,j