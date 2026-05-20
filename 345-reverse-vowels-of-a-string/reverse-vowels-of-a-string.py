class Solution(object):
    def reverseVowels(self, s):
        s=list(s)
        p=["a","e","i","o","u","A","E","I","O","U"]
        l=0
        r=len(s)-1
        while l<r:
            if s[l] not in p:
                l+=1
            elif s[r] not in p:
                r-=1
            else:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
        return "".join(s)

        