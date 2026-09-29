class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        n=len(nums)
        n_l=[]
        dict={}
        for i in range(len(nums)):
                if nums[i] in dict:
                    dict[nums[i]]+=1
                else:
                    dict[nums[i]]=1
        for i,j in dict.items():
            if j>n/3:
                n_l.append(i)
        return n_l

        