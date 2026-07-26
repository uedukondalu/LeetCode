class Solution(object):
    def maximumProduct(self, nums):
        n=nums
        m1=m2=m3=float('-inf')
        mi=mi2=float('inf')
        for i in n:
            if i>m1:
                m3=m2
                m2=m1
                m1=i
            elif i>m2:
                m3=m2
                m2=i
            elif i>m3:
                m3=i
            if i<mi:
                mi2=mi
                mi=i
            elif i<mi2:
                mi2=i
        return max(m1*m2*m3,mi*mi2*m1)        
        
