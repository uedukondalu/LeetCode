class Solution(object):
    def sumOfGoodIntegers(self, n, k):
        
        c=0
        for i in range(max(1,n-k),n+k+1) :
            s=abs(n-i)
            r=n&i
            if s<=k and r==0:
                c+=i
            i+=1
        return c 