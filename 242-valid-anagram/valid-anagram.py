class Solution(object):
    def isAnagram(self, s, t):
        f={}
        for i in s:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        f2={}
        for i in t:
            if i in f2:
                f2[i]+=1
            else:
                f2[i]=1
        if f==f2:
            return True
        else:
            return False