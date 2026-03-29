class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        fre=[]
        for i in range(len(nums)):
            fre.append(nums[i]*nums[i])
            fre.sort()
        return fre

        