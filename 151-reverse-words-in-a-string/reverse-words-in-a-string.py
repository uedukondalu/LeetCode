class Solution(object):
    def reverseWords(self, s):
        r=s.split()
        re=r[::-1]
        s=" ".join(re)
        return s