class Solution(object):
    def minElement(self, nums):
        n=nums
        f=[]
        for i in n:
            s=0
            for j in str(i):
                s+=int(j)
            f.append(s)
        return min(f)
        