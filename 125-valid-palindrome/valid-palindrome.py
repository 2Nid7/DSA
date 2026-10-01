class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        start=0
        end=len(s)-1
        while start<=end:
            if s[start].isalnum()==False:
                start=start+1
            elif s[end].isalnum()==False:
                end=end-1
            elif s[start]!=s[end]:
                return False
            else:
                start=start+1
                end-=1
        return True





