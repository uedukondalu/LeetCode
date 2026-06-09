class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        i=max(1,n-k)
        c=0
        while i<=n+k:
            s=abs(n-i)
            if s<=k:
                r=n&i
                if s<=k and r==0:
                    c+=i
            i+=1
        return c 