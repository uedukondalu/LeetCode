class Solution(object):
    def minimumTotal(self, triangle):
        r=triangle
        for i in range(len(r)-2,-1,-1):
            for j in range(len(r[i])):
                r[i][j]+=min(r[i+1][j],r[i+1][j+1])
        return r[0][0]
        