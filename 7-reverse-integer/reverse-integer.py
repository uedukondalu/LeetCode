class Solution(object):
    def reverse(self, x):
        s=0
        if x<0:
            s=-1
        else:
            s=1
        x=abs(x)
        x=str(x) [::-1]
        r=int(x)*s
        if r<-2**31 or r>2**31-1:
            return 0
        return r
