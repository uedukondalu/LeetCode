class Solution(object):
    def lastStoneWeight(self, stones):
        s=stones
        while(len(s)>1):
            s.sort(reverse=True)
            y=s.pop(0)
            x=s.pop(0)
            if y!=x:
                s.append(y-x)
        if s:
            return s[0]
        return 0

