class Solution(object):
    def smallestNumber(self, n, t):
        while True:
            r=1
            for i in str(n):
                r*=int(i)
            if r%t==0:
                return n
            n+=1
