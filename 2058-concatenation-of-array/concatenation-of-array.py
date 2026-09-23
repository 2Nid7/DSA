class Solution:
    def getConcatenation(self, nums: list[int]) -> list[int]:
        n_l=[]
        for i in nums:
            n_l.append(i)
        for i in n_l:
            nums.append(i)
        return nums
        