class Solution(object):
    def jump(self, nums):
        n=nums
        f=0
        c=0
        j=0
        for i in range(len(n)-1):
            f=max(f,i+n[i])
            if i==c:
                j+=1
                c=f
        return j
        