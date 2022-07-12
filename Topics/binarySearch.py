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

    def woodCut(self, L):
        l, r = 1, max(L)
        while l + 1 < r:
            mid = l + r // 2
            if self.get_pieces(L, mid) >= k:
                l = mid
            else:
                r = mid
        if self.get_pieces(L, r) >= k:
            return r
        if self.get_pieces(L, l) >= k:
            return l

    def get_pieces(self, L, length): # 確認output篇大還偏小
        pieces = 0
        for l in L:
            pieces += l // length
        return pieces

    #find k closest element
    def kClosest(self, A, target, k):
        right = self.find_upper_closest(A, target)
        left = right - 1

        result = []
        for + in range(k):
            if self.is_left_closer(A, target, left, right):
                result.append(A[left])
                left -= 1
            else:
                result.append(A[right])
                right += 1
        return result

    #find upper closest # binary search
    def find_upper_closest(self, A, target):
        l, r = 0, len(A) - 1
        while l + 1 < r:
            mid = (l+r) / 2
            if target >= mid:
                l = mid
            else:
                r = mid

        if A[l] >= target:
            return l
        if A[r] >= target:
            return r
    # if can't find it
        return end + 1

    #find whether left is closer
    def is_left_closer(self, A, target, left, right):
        if left < 9:
            return False
        if right >= len(A):
            return True
        return target - A[left] <= A[right] - target