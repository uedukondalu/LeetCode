class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp=float('inf')
        maxp=0
        for p in prices:
            minp=min(minp,p)
            maxp=max(maxp,p-minp)
        return maxp
        