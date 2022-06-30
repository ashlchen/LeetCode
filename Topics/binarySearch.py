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

    def findMin(self, nums: List[int]) -> int:
    # two pointer
    l, r = 0, len(nums) - 1
    if len(nums)==1:
        return nums[0]
    if nums[0] < nums[r]:
        return nums[0]
    # mid
    while l <= r:
        mid = (l+r) // 2
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        elif nums[mid] < nums[mid - 1]:
            return nums[mid]
        elif nums[l] <= nums[mid]:
            l = mid
        else:
            r = mid - 1
    # smaller should be right after the peak
    
    #edge
    #[0]
    #[2,1]