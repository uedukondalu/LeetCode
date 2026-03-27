from collections import Counter
class Solution(object):
    def isAnagram(self, s, t):
        sp=Counter(s)
        tp=Counter(t)
        if sp==tp:
            return(True)
        else:
            return(False)

        