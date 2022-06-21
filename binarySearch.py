class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # binary search to have time log n
        
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l+r) //2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                if nums[mid] <= target <=nums[r]:
                    l = mid
                else:
                    r = mid - 1
        
        return -1