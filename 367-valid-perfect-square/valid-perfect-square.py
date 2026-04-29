class Solution(object):
    def isPerfectSquare(self, num):
        a=num**0.5
        if a%1==0:
            return True
        else:
            return False