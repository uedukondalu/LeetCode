class Solution(object):
    def minimumCost(self, cost):
        c=sorted(cost,reverse=True)
        t=0
        for i in range(len(c)):
            if  (i+1)%3!=0:
                t+=c[i]
        return t
