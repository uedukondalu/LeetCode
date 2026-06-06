class Solution(object):
    def digitFrequencyScore(self, n):
        ch={}
        for i in str(n):
            if i in ch:
                ch[i]+=1
            else:
                ch[i]=1
        t=0
        for i,j in ch.items():
            t+=int(i)*j
        
        return t
