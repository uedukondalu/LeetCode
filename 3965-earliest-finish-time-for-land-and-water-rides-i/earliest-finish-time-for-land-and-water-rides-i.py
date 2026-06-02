class Solution(object):
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration):
        l=landStartTime
        l1=landDuration
        w=waterStartTime
        w1=waterDuration
        a=float("inf")
        for i in range(len(l)):
            for j in range(len(w)):
                r=l[i]+l1[i]
                r1=max(r,w[j])+w1[j]
                a=min(a,r1)
                f=w[j]+w1[j]
                f1=max(f,l[i])+l1[i]
                a=min(a,f1)
        return a
        