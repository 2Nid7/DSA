class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        pos=0
        neg=1
        k=[0]*len(nums)
        for num in nums:
            if num>0:
                k[pos]=num
                pos+=2
            else:
                k[neg]=num
                neg+=2
        return k 
        