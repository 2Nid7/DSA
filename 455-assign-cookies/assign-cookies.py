class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s.sort()
        g.sort()
        slen=len(s)
        i=0
        g1=len(g)
        j=0
        cnt=0
        while i<slen and j<g1:
            if s[i]>=g[j]:
                cnt+=1
                j+=1
            i+=1
        return cnt

        