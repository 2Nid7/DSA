class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dct={}
        for i,numb in enumerate(nums):
            req=target-numb
            if req in dct:
                return [i,dct[req]]
            dct[numb]=i
        

        