class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i, num in enumerate(nums):
            temp = num
            