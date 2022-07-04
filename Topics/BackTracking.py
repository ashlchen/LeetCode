
class Solution:
    def subsets(self, nums):
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

    def combinationSum(self, nums, target):
        result = []
        def backtrack(nextNumIndex, curArray, curSum):
            if curSum == target:
                result.append(curArray.copy())
                return
            elif curSum > target or nextNumIndex >= len(nums):
                return
            curArray.append(nums[nextNumIndex])
            backtrack(nextNumIndex, curArray, curSum+nums[nextNumIndex])
            curArray.pop()
            backtrack(nextNumIndex+1, curArray, curSum)
        backtrack(0, [], 0)
        return result
    
Object = Solution()
print(Object.combinationSum([2,3,5], 7))


