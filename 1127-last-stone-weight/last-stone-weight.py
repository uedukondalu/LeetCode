class Solution(object):
    def lastStoneWeight(self, stones):
        s=stones
        while len(s)>1:
            s.sort(reverse=True)
            p=s.pop(0)
            q=s.pop(0)
            if q!=p:
                s.append(p-q)
        if s:
            return s[0]
        return 0

