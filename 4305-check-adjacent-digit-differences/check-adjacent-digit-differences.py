class Solution(object):
    def isAdjacentDiffAtMostTwo(self, s):
        s=[int(i) for i in str(s)]
        r=[]
        for i in range(len(s)-1):
            r.append(abs(s[i+1]-s[i]))
        for i in r:
            if i>2:
                return False
        return True
