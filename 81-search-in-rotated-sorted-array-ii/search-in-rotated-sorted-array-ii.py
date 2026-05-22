class Solution(object):
    def search(self, nums, target):
        t=target
        n=sorted(nums)
        f=[]
        for i in range(len(n)):
            if n[i] not in f:
                f.append(n[i])
        l=0
        r=len(f)-1
        while l<=r:
            m=(l+r)//2
            if f[m]==t:
                return True
            elif f[m]<t:
                l=m+1
            else:
                r=m-1
        return False
