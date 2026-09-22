class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n=len(nums)
        l={}
        for i in nums:
            if i in l:
                l[i]+=1
            else:
                l[i]=1
        for key,value in l.items():
            if value > n/2:
                return key
            

        
        