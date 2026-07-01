class Solution(object):
    def transpose(self, matrix):
        m=matrix
        r=[]
        for i in range(len(m[0])):
            f=[]
            for j in range(len(m)):
                f.append(m[j][i])
            r.append(f)
        return  r