class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct={}
        if len(s)!=len(t):
            return False
        for i in s:
            dct[i]=dct.get(i,0)+1
        for ch in t:
            dct[ch]=dct.get(ch,0)-1
        for k in dct.values():
            if k!=0:
                return False
        return True
        
            
            




