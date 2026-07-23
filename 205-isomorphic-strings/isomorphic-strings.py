class Solution(object):
    def isIsomorphic(self, s, t):
        if len(s)!=len(t):
            return False
        f={}
        f2={}
        for i in range(0,len(s)):
            c1=s[i]
            c2=t[i]
            if c1 in f:
                if f[c1]!=c2:
                    return False
            else:
                f[c1]=c2
            if c2 in f2:
                if f2[c2]!=c1:
                    return False
            else:
                f2[c2]=c1
        return True

            

        