class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        def backtrack(nums):
            if not nums:
                return
            # add to the result
            if nums not in res:
                res.append(nums.copy())
            # take out each of the element
                for i, num in enumerate(nums):
                # call backtrack
                    backtrack(nums[:i] + nums[i+1:])
        backtrack(nums)
        return res