class Solution(object):
    def missingNumber(self, nums):
        s=sorted(nums)
        for i in range(0,len(s)):
            if i!=s[i]:
                return i
        return len(s)
      