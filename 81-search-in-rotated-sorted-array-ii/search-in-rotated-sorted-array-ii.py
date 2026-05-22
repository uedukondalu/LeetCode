class Solution(object):
    def search(self, nums, target):
        t=target
        n=sorted(nums)
        for i in range(len(n)):
            if n[i]==target:
                return True
        return False